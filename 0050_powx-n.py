# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-26 23:22
# software: PyCharm
"""
题目：Pow(x, n)

实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages


# 基础的次幂**
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x ** n


# 快速幂
# 向下整数 n // 2 等价于 右移一位 n >> 1
# 取余数 n % 2 等价于 判断二进制最右一位值 n & 1
class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0: return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res


# 减少递归次数
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        def result(x, n):
            if n == 1:
                return x
            num = result(x, n // 2)
            if n % 2 == 0:  # n为偶数时
                return num * num
            else:  # n 为奇数时
                return num * num * x

        if n == 0:
            return 1
        if n < 0:
            return 1 / result(x, -n)
        return result(x, n)


if __name__ == '__main__':
    x, n = 2.00000, 10
    solution = Solution()
    res = solution.myPow(x, n)
    print(res)

    solution1 = Solution1()
    res1 = solution1.myPow(x, n)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.myPow(x, n)
    print(res2)