# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-25 22:41
# software: PyCharm
"""
题目：递增子序列

给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 动态规划+哈希表
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        pres = {(nums[0],)}
        for i in nums[1:]:
            pres.update({j + (i,) for j in pres if j[-1] <= i})
            pres.add((i,))
        return [list(i) for i in pres if len(i) > 1]


# 组合
import itertools


class Solution1(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        for i in range(2, len(nums) + 1):
            for j in itertools.combinations(nums, i):
                if j != tuple(sorted(j)):
                    continue
                if j not in res:
                    res.add(j)

        return [list(s) for s in res]


# 深度优先搜索+哈希表
class Solution2(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(nums, tmp):
            if len(tmp) > 1:
                res.append(tmp)
            ans = set()
            for k, v in enumerate(nums):
                if v in ans:
                    continue
                if not tmp or v >= tmp[-1]:
                    ans.add(v)
                    dfs(nums[k + 1:], tmp + [v])

        dfs(nums, [])
        return res


# 广度优先搜索+哈希表
import collections


class Solution3(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque([(nums, [])])
        while q:
            cur, new = q.popleft()
            if len(new) > 1:
                res.append(new)
            ans = set()
            for k, v in enumerate(cur):
                if v in ans:
                    continue
                if not new or v >= new[-1]:
                    ans.add(v)
                    q.append((cur[k + 1:], new + [v]))
        return res


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    solution = Solution()
    res = solution.findSubsequences(nums)
    print(res)

    solution1 = Solution1()
    res1 = solution1.findSubsequences(nums)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.findSubsequences(nums)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.findSubsequences(nums)
    print(res3)
