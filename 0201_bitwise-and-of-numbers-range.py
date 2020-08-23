# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-23 19:45
# software: PyCharm
"""
题目：数字范围按位与

给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 位移，找公共前缀
# 时间复杂度：O(logn)，空间复杂度：O(1)
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            res += 1
        return m << res


# Brian Kernighan算法
# 时间复杂度：O(logn)，空间复杂度：O(1)
class Solution1(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
            n = n & (n - 1)
        return n


if __name__ == '__main__':
    r = [5, 7]
    m, n = r[0], r[1]
    solution = Solution()
    res = solution.rangeBitwiseAnd(m, n)
    print(res)

    solution1 = Solution1()
    res1 = solution1.rangeBitwiseAnd(m, n)
    print(res1)
