# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-26 14:46
# software: PyCharm
"""
题目：位1的个数

编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

示例 1：

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
示例 2：

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
示例 3：

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 转化为二进制，并count
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)  # 转化为二进制
        return num.count('1')


# 转化为二进制，循环计算1的个数
class Solution1(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = bin(n)
        count = 0
        for i in num:
            if i == '1':
                count += 1
        return count


# 转化为二进制时，求余判断是否为1
class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            res = n % 2
            if res == 1:
                count += 1
            n //= 2
        return count


# 使用位运算
class Solution3(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


if __name__ == '__main__':
    n = 11
    solution = Solution()
    res = solution.hammingWeight(n)
    print(res)

    solution1 = Solution1()
    res1 = solution1.hammingWeight(n)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.hammingWeight(n)
    print(res2)

    solution2 = Solution2()
    res2 = solution2.hammingWeight(n)
    print(res2)
