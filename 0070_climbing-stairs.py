# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-9 2:10
# software: PyCharm
"""
题目：爬楼梯

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
import functools  # 调试时估计不让导入模块，而且常规递归容易超时


# 直接递归法，容易超时，加入缓存装饰器，递归转换成迭代
class Solution1(object):
    @functools.lru_cache(100)  # 缓存装饰器
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# 数组记忆递归法，减少重复计算
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [-1 for i in range(n + 1)]
        if n == 1: return 1
        if n == 2: return 2
        if nums[n] == -1:
            nums[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return nums[n]


# 直接DP，利用字典存储变量
class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# DP，存储元素交换，建议用一个临时变量temp，使得a,b a+b进行交换，这样更节省时间
class Solution4(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        if n == 2: return 2
        a, b = 1, 2
        for i in range(3, n + 1):
            b, a = a + b, b
        return b


# 直接用斐波那契数列的计算公式
import math
class Solution5(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = 5 ** 0.5
        fib = math.pow((1+sqrt5)/2, n+1)- math.pow((1-sqrt5)/2, n+1)
        return int(fib/sqrt5)

if __name__ == '__main__':
    n = 7
    solution1 = Solution1()
    res1 = solution1.climbStairs(n)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.climbStairs(n)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.climbStairs(n)
    print(res3)

    solution4 = Solution4()
    res4 = solution4.climbStairs(n)
    print(res4)

    solution5 = Solution5()
    res5 = solution5.climbStairs(n)
    print(res5)
