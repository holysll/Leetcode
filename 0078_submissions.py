# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-9-20 23:52
# software: PyCharm
"""
题目：子集

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
# 排列组合
# https://www.cnblogs.com/xiao-apple36/p/10861830.html
# 利用itertools.combinations(iterable, r)
import itertools
class Solution(object):
    def subsets(self, nums):
        res = []
        for i in range(len(nums)+1):
            for j in itertools.combinations(nums,i):
                res.append(list(j))
        return res

import functools
class Solution1(object):
    def subsets(self, nums):
        return functools.reduce(lambda x,j: x+[i + [j] for i in x], nums, [[]])


if __name__ == '__main__':
    nums = [1,2,3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)

    solution1 = Solution1()
    res1 = solution1.subsets(nums)
    print(res1)
