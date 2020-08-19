# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-19 20:50
# software: PyCharm
"""
题目：回文子串

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"

提示：

输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 暴力求解，循环切片
# 时间复杂度：O(n^3)，空间复杂度：O(1)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                char = s[i:j + 1]
                if char == char[::-1]:
                    count += 1
        return count


# 动态规划-中心扩散法
# 时间复杂度：O(n^2)，空间复杂度：O(n^2)
class Solution1(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = 1
                    res += 1
        return res


# 中心扩散法
# 时间复杂度：O(n^2)，空间复杂度：O(1)
class Solution2(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        # 奇数子串情况
        for i in range(len(s)):
            res += self.expand(s, i, i)
        # 偶数子串情况
        for j in range(len(s)):
            res += self.expand(s, j, j + 1)

        return res

    def expand(self, s, l, r):
        count = 0
        # 下标不越界且为回文子串
        while l >= 0 and r <= len(s)-1 and s[l] == s[r]:
            l -= 1  # 左边-1
            r += 1  # 右边+1
            count += 1  # 回文计数+1
        return count


if __name__ == '__main__':
    s = "aaa"
    solution = Solution()
    res = solution.countSubstrings(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.countSubstrings(s)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.countSubstrings(s)
    print(res2)
