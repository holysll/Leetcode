# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-1 18:35
# software: PyCharm
"""
题目：转换成小写字母

实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

 

示例 1：

输入: "Hello"
输出: "hello"
示例 2：

输入: "here"
输出: "here"
示例 3：

输入: "LOVELY"
输出: "lovely"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/to-lower-case
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages

# 我的解法
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ""
        for i in str:
            if i.isupper():
                res += i.lower()
            else:
                res += i
        return res


# 内置函数
class Solution1(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


# 利用ASCII码值和ord()函数
class Solution2(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join([chr(ord(i)+32) if ord(i) > 65 and ord(i) <= 90 else i for i in str])


# 利用ASCII码值和ord()函数
# 'A' - 'Z' 对应的 ascii 是 65 - 90；
# 'a' - 'z' 对应的 ascii 是 97 - 122；
class Solution3(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for i in str:
            if 65 <= ord(i) <= 90:
                res += chr(ord(i) + 32)
            else:
                res += i
        return res


if __name__ == '__main__':
    s = "LOVELY"
    solution = Solution()
    res = solution.toLowerCase(s)
    print(res)

    solution1 = Solution1()
    res1 = solution1.toLowerCase(s)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.toLowerCase(s)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.toLowerCase(s)
    print(res3)