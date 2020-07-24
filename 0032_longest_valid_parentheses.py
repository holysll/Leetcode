# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-4 23:54
# software: PyCharm

"""
题目：最长有效括号

给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 使用栈
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)

        res.sort()
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1

        return ans


# 使用栈，优化
class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0  # 最大有效括号长度
        stack = [-1]  # stack[0]:合法括号起点-1 ; stack[1:]尚未匹配左括号下标
        for i in range(len(s)):
            if s[i] == "(":  # 左括号
                stack.append(i)
            else:  # 右括号，且有成对的左括号
                stack.pop()  # 弹出左括号
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])
        return res


# 动态规划
class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i > 0 and s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res


if __name__ == '__main__':
    s = ")()())"
    solution = Solution()
    res = solution.longestValidParentheses(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.longestValidParentheses(s)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.longestValidParentheses(s)
    print(res2)
