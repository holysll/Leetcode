# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-1 22:34
# software: PyCharm
"""
题目：最小区间

你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

示例 1:

输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出: [20,24]
解释:
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
注意:

给定的列表可能包含重复元素，所以在这里升序表示 >= 。
1 <= k <= 3500
-105 <= 元素的值 <= 105
对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python package

# 最小堆+指针
# 时间复杂度：0(nk log k)，空间复杂度：O(k)

import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        L, R = -10 ** 9, 10 ** 9
        max_val = max(val[0] for val in nums)
        queue = [(val[0], i, 0) for i, val in enumerate(nums)]
        heapq.heapify(queue)

        while True:
            min_val, row, index = heapq.heappop(queue)
            if max_val - min_val < R - L:
                L, R = min_val, max_val
            if index == len(nums[row]) - 1:
                break
            max_val = max(max_val, nums[row][index + 1])
            heapq.heappush(queue, (nums[row][index + 1], row, index + 1))

        return [L, R]


# 哈希表 + 滑动窗口
# 时间复杂度：O(nk + |V|)，空间复杂度：O(nk)
import collections


class Solution1(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        dic = collections.defaultdict(list)
        min_val, max_val = 10 ** 9, -10 ** 9
        for k, v in enumerate(nums):
            for i in v:
                dic[i].append(k)
            min_val = min(min_val, *v)
            max_val = max(max_val, *v)

        count = [0] * n
        inside = 0
        left, right = min_val, min_val - 1
        L, R = min_val, max_val

        while right < max_val:
            right += 1
            if right in dic:
                for j in dic[right]:
                    count[j] += 1
                    if count[j] == 1:
                        inside += 1
                while inside == n:
                    if right - left < R - L:
                        L, R = left, right
                    if left in dic:
                        for s in dic[left]:
                            count[s] -= 1
                            if count[s] == 0:
                                inside -= 1
                    left += 1

        return [L, R]



if __name__ == '__main__':
    nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    solution = Solution()
    res = solution.smallestRange(nums)
    print(res)

    solution1 = Solution1()
    res1 = solution1.smallestRange(nums)
    print(res1)
