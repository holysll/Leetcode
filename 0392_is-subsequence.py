# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-27 1:35
# software: PyCharm
"""
题目：判断子序列

给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

示例 1:
s = "abc", t = "ahbgdc"

返回 true.

示例 2:
s = "axc", t = "ahbgdc"

返回 false.

后续挑战 :

如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
import sys


# 双指针
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m


# 动态规划
class Solution1:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[0] * 26 for _ in range(n)]
        dp.append([n] * 26)

        for i in range(n - 1, -1, -1):
            for j in range(26):
                if ord(t[i]) == j + ord('a'):
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
        res = 0
        for i in range(m):
            if dp[res][ord(s[i]) - ord('a')] == n:
                return False
            res = dp[res][ord(s[i]) - ord('a')] + 1

        return True


# 递归
class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return False
        for j in range(len(t)):
            if s[0] == t[j]:
                if len(s) == 1:
                    return True
                return self.isSubsequence(s[1:], t[j + 1:])
        return False


# 利用find函数
class Solution3:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        loc = -1
        for i in s:
            loc = t.find(i, loc + 1)
            if loc == -1:
                return False
        return True

# 利用迭代器，调用内部__next__()方法
class Solution4:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)


if __name__ == '__main__':
    s = "axc"
    t = "ahbgdc"
    solution = Solution()
    res = solution.isSubsequence(s, t)
    print(res)

    solution1 = Solution1()
    res1 = solution1.isSubsequence(s, t)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.isSubsequence(s, t)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.isSubsequence(s, t)
    print(res3)
