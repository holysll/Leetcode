# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-23 1:14
# software: PyCharm
"""
题目：整数拆分

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import math


# 数学递推
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3
        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a - 1) * 4)
        else:
            return int(math.pow(3, a) * 2)


# 动态规划
class Solution1(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(j * dp[i - j], j * (i - j), dp[i])

        return dp[n]


# 记忆化技术（自顶向下）
class Solution2(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0 for i in range(n + 1)]

        def func(n):
            if n == 2:
                return 1
            if f[n] != 0:
                return f[n]
            res = -1
            for i in range(1, n):
                res = max(res, max(i * (n - i), i * func(n - i)))
            f[n] = res
            return res
        return func(n)


if __name__ == '__main__':
    n = 10
    solution = Solution()
    res = solution.integerBreak(n)
    print(res)

    solution1 = Solution1()
    res1 = solution1.integerBreak(n)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.integerBreak(n)
    print(res2)
