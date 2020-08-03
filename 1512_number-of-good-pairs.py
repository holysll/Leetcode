# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-3 19:04
# software: PyCharm
"""
题目：好数对的数目

给你一个整数数组 nums 。

如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。

返回好数对的数目。

示例 1：

输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
示例 2：

输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对
示例 3：

输入：nums = [1,2,3]
输出：0

提示：

1 <= nums.length <= 100
1 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-good-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Python packages


# 个人解法，结果放入新的列表
import collections


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    res.append((i, j))
        return len(res)


# 两次遍历进行循环
class Solution1(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count


# 组合计数
class Solution2(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.Counter(nums)
        return sum(v * (v - 1) // 2 for k, v in dic.items())


# 暴力统计相同元素的个数
class Solution3(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([nums[k + 1:].count(v) for k, v in enumerate(nums)])


# 哈希表
from collections import defaultdict
class Solution4(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, dic = 0, defaultdict(int)
        for i in nums:
            res, dic[i] = res + dic[i], dic[i] + 1
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    solution = Solution()
    res = solution.numIdenticalPairs(nums)
    print(res)

    solution1 = Solution1()
    res1 = solution1.numIdenticalPairs(nums)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.numIdenticalPairs(nums)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.numIdenticalPairs(nums)
    print(res3)

    solution4 = Solution4()
    res4 = solution4.numIdenticalPairs(nums)
    print(res4)
