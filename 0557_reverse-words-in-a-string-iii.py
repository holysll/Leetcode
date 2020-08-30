# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-30 21:31
# software: PyCharm
"""
题目：反转字符串中的单词 III

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 自己版本
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # return " ".join([word[::-1] for word in s.split(" ")])
        # return ' '.join(map(lambda word: word[::-1], s.split()))
        return ' '.join(s[::-1].split(' ')[::-1])


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    solution = Solution()
    res = solution.reverseWords(s)
    print(res)