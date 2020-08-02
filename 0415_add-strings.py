# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-3 0:26
# software: PyCharm
"""
题目：字符串相加

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval(num1) + eval(num2))


# 双指针
"""
解题思路：
算法流程： 设定 i，j 两指针分别指向 num1，num2 尾部，模拟人工加法；

计算进位： 计算 carry = tmp // 10，代表当前位相加是否产生进位；
添加当前位： 计算 tmp = n1 + n2 + carry，并将当前位 tmp % 10 添加至 res 头部；
索引溢出处理： 当指针 i或j 走过数字首部后，给 n1，n2 赋值为 00，相当于给 num1，num2 中长度较短的数字前面填 00，以便后续计算。
当遍历完 num1，num2 后跳出循环，并根据 carry 值决定是否在头部添加进位 11，最终返回 res 即可。

作者：jyd
链接：https://leetcode-cn.com/problems/add-strings/solution/add-strings-shuang-zhi-zhen-fa-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution1(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


# 无int，利用ASCII转换
class Solution2(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 or j >= 0:
            n1 = num1[i] if i >= 0 else "0"
            n2 = num2[j] if j >= 0 else "0"
            tmp = ord(n1) + ord(n2) - 2 * ord("0") + carry
            carry = tmp // 10
            res = chr((tmp % 10) + 48) + res
            i -= 1
            j -= 1
        return "1" + res if carry else res


# 大数相加
class Solution3(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        res = ""
        carry = 0
        while m > n:
            num2 = "0" + num2
            n += 1
        while m < n:
            num1 = "0" + num1
            m += 1
        for i in range(m - 1, -1, -1):
            a = int(num1[i])
            b = int(num2[i])
            tmp = a + b + carry
            res = str(tmp % 10) + res
            carry = tmp // 10
        if carry:
            return "1" + res
        else:
            return res


if __name__ == '__main__':
    num1 = "21"
    num2 = "100"
    solution = Solution()
    res = solution.addStrings(num1, num2)
    print(res)

    solution1 = Solution1()
    res1 = solution1.addStrings(num1, num2)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.addStrings(num1, num2)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.addStrings(num1, num2)
    print(res3)
