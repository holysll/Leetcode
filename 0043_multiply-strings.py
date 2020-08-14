# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-13 14:37
# software: PyCharm
"""
题目：字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 利用eval()偷懒解法
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(eval(num1 + "*" + num2))


# 做加法
# 时间复杂度：O(mn+n^2), 空间复杂度：O(m+n)
class Solution1(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        res = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            nums = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                nums.append(str(product % 10))
                add = product // 10
            if add > 0:
                nums.append(str(add))
            nums = "".join(nums[::-1])
            res = self.addStrings(res, nums)
        return res

    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        res = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            res.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(res[::-1])


# 做乘法，用数组存储
# 时间复杂度：O(mn), 空间复杂度：O(m+n)
class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        nums = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                nums[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            nums[i - 1] += nums[i] // 10
            nums[i] %= 10

        index = 1 if nums[0] == 0 else 0
        res = "".join(str(x) for x in nums[index:])
        return res


class Solution3(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = num1[::-1]
        b = num2[::-1]
        res = 0

        for k1, v1 in enumerate(a):
            tmp = 0
            for k2, v2 in enumerate(b):
                tmp += int(v1) * int(v2) * 10 ** k2
            res += tmp * 10 ** k1

        return str(res)

if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    solution = Solution()
    res = solution.multiply(num1, num2)
    print(res)

    solution1 = Solution1()
    res1 = solution1.multiply(num1, num2)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.multiply(num1, num2)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.multiply(num1, num2)
    print(res3)
