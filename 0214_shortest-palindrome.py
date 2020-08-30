# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-29 23:15
# software: PyCharm
"""
题目：最短回文串

给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

示例 1:

输入: "aacecaaa"
输出: "aaacecaaa"
示例 2:

输入: "abcd"
输出: "dcbabcd"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shortest-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 字符串哈希
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        base, mod = 131, 10 ** 9 + 7
        left = right = 0
        mul = 1
        best = -1

        for i in range(n):
            left = (left * base + ord(s[i])) % mod
            right = (right + mul * ord(s[i])) % mod
            if left == right:
                best = i
            mul = mul * base % mod

        add = ("" if best == n - 1 else s[best + 1:])
        return add[::-1] + s


# KMP算法
class Solution1(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        fail = [-1] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j != -1 and s[j + 1] != s[i]:
                j = fail[j]
            if s[j + 1] == s[i]:
                fail[i] = j + 1

        best = -1
        for i in range(n - 1, -1, -1):
            while best != -1 and s[best + 1] != s[i]:
                best = fail[best]
            if s[best + 1] == s[i]:
                best += 1

        add = ("" if best == n - 1 else s[best + 1:])
        return add[::-1] + s


# 枚举
class Solution2(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(reverse[i:]):
                return reverse[:i] + s


if __name__ == '__main__':
    s = "aacecaaa"
    solution = Solution()
    res = solution.shortestPalindrome(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.shortestPalindrome(s)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.shortestPalindrome(s)
    print(res2)
