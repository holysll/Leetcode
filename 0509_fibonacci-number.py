# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-8 14:02
# software: PyCharm
"""
题目：斐波那契数
通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。
也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.
 

提示：

0 ≤ N ≤ 30

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fibonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
# 标准递归解法：（要超时）
class Solution1(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        return (self.fib(n-1)+self.fib(n-2))%1000000007


# 数组备忘的递归解法
class Solution2(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [-1 for i in range(n+1)]  # 记录计算的值
        if n == 0:
            return 0
        if n == 1:
            return 1
        if nums[n] == -1:
            nums[n] = self.fib(n-1) + self.fib(n-2)
        return nums[n]

# DP解法：解决记忆化递归消耗内存的问题
class Solution3(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[0] = 0
        dp[1] = 1
        if n >= 2:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n] % 1000000007


# 优化DP解法
class Solution4(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007


# 利用列表
class Solution5(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [0, 1]
        for i in range(2, n + 1):
            s.append(s[-1] + s[-2])
        return s[n] % 1000000007


if __name__ == "__main__":
    n = 3
    solution1 = Solution1()
    res1 = solution1.fib(n)
    print(res1)
    
    solution2 = Solution2()
    res2 = solution2.fib(n)
    print(res2)
    
    solution3 = Solution3()
    res3 = solution3.fib(n)
    print(res3)
    
    solution4 = Solution4()
    res4 = solution4.fib(n)
    print(res4)
