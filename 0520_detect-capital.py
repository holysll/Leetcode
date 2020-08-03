# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-3 14:15
# software: PyCharm
"""
题目：检测大写字母

给定一个单词，你需要判断单词的大写使用是否正确。

我们定义，在以下情况时，单词的大写用法是正确的：

全部字母都是大写，比如"USA"。
单词中所有字母都不是大写，比如"leetcode"。
如果单词不只含有一个字母，只有首字母大写， 比如 "Google"。
否则，我们定义这个单词没有正确使用大写字母。

示例 1:

输入: "USA"
输出: True
示例 2:

输入: "FlaG"
输出: False
注意: 输入是由大写和小写拉丁字母组成的非空单词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/detect-capital
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 我的暴力解法
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():  # 全为大写或者小写
            return True
        elif word[0].isupper() and word[1:].islower():  # 首字母大写，其他小写
            return True
        else:
            return False


# istitle():检测字符串中所有的单词拼写首字母是否为大写
class Solution1(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or word.istitle()


# 正则大佬解法
import re


class Solution2(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return True if re.match(r'(([A-Z]+)|([A-Z]?[a-z]+))$', word) else False


# 常规判断字母
class Solution3(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        count = 0
        for i in word:
            if i in s:
                count += 1
        if count == 0 or count == len(word) or (count == 1 and word[0] in s):
            return True
        return False


if __name__ == '__main__':
    word = "GGoogle"
    solution = Solution()
    res = solution.detectCapitalUse(word)
    print(res)

    solution1 = Solution1()
    res1 = solution1.detectCapitalUse(word)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.detectCapitalUse(word)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.detectCapitalUse(word)
    print(res3)
