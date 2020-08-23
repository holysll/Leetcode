# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-22 22:13
# software: PyCharm
"""
题目：24点游戏

你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。

示例 1:

输入: [4, 1, 8, 7]
输出: True
解释: (8-4) * (7-1) = 24
示例 2:

输入: [1, 2, 1, 2]
输出: False
注意:

除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。
每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允许的。
你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/24-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
import itertools

import math


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = 24
        region = 1e-6
        add, multiply, subtract, divide = 0, 1, 2, 3

        def solve(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - target) < region
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for m in range(4):
                            if m < 2 and i > j:
                                continue
                            if m == add:
                                newNums.append(x + y)
                            elif m == multiply:
                                newNums.append(x * y)
                            elif m == subtract:
                                newNums.append(x - y)
                            elif m == divide:
                                if abs(y) < region:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)


class Solution1(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return math.isclose(nums[0], 24)
        return any(self.judgePoint24([x] + rest) for a, b, *rest in itertools.permutations(nums) for x in
                   {a + b, a - b, a * b, b and a / b})


if __name__ == '__main__':
    nums = [8, 1, 6, 6]
    solution = Solution()
    res = solution.judgePoint24(nums)
    print(res)

    nums = [8, 1, 6, 6]
    solution1 = Solution1()
    res1 = solution1.judgePoint24(nums)
    print(res1)
