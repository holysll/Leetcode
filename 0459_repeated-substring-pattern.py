# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-24 21:32
# software: PyCharm
"""
题目： 重复的子字符串

给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"

输出: True

解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"

输出: False
示例 3:

输入: "abcabcabcabc"

输出: True

解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-substring-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 枚举
# 时间复杂度：O(n^2)，空间复杂度：O(1)
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False


# 字符串匹配
class Solution1(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s + s).find(s, 1) != len(s)


# KMP算法
# 时间复杂度：O(n)，空间复杂度：O(n)
class Solution2(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def kmp(query, pattern):
            n, m = len(query), len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1

            match = -1
            for i in range(1, n - 1):
                while match != -1 and pattern[match + 1] != query[i]:
                    match = fail[match]
                if pattern[match + 1] == query[i]:
                    match += 1
                    if match == m - 1:
                        return True
            return False

        return kmp(s + s, s)


if __name__ == '__main__':
    s = "abcabcabcabc"
    solution = Solution()
    res = solution.repeatedSubstringPattern(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.repeatedSubstringPattern(s)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.repeatedSubstringPattern(s)
    print(res2)
