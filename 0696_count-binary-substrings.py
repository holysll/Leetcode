# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-10 1:43
# software: PyCharm
"""
题目：计数二进制子串

给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
示例 2 :

输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
注意：

s.length 在1到50,000之间。
s 只包含“0”或“1”字符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 一次遍历，其实就是找出所有01连续组合的统计数
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        last = ""
        j = k = 0
        for i in s:
            if last == i:
                j += 1
            else:
                last = i
                res += min(j, k)
                k, j = j, 1
        return res + min(j, k)


# 1、计算当前这个与前面字符是否相同，并记录个数，curLen
# 2、when当前的字符与前面的字符不相同时，将前面字符的个数保存,preLen
# 3、当preLen>=curLen时，说明存在01和0011这两种情况中的一种，所以个数count=1
class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        res = 0  # 记录子串的个数
        m = 1  # 当前这个与前面字符是相同个数
        n = 0  # 当前的字符与前面的字符不相同个数
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                m += 1
            else:
                # res += min(m, n)
                m, n = 1, m
            if n >= m:
                res += 1
        return res
        # return res + min(m, n)


if __name__ == '__main__':
    s = "00110011"
    solution = Solution()
    res = solution.countBinarySubstrings(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.countBinarySubstrings(s)
    print(res1)
