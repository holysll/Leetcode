# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-30 11:46
# software: PyCharm
"""
题目：反转字符串

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 利用reverse()函数
class Solution:
    def reverseString(self, s):
        s.reverse()
        return s


# 递归
class Solution1:
    def reverseString(self, s):
        def func(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                func(l + 1, r - 1)
        func(0, len(s)- 1)
        return s


# 双指针
class Solution2:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


# 列表切片
class Solution3:
    def reverseString(self, s):
        return s[::-1]


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    solution = Solution()
    res = solution.reverseString(s)
    print(res)

    s1 = ["h", "e", "l", "l", "o"]
    solution1 = Solution1()
    res1 = solution1.reverseString(s1)
    print(res1)

    s2 = ["h", "e", "l", "l", "o"]
    solution2 = Solution2()
    res2 = solution2.reverseString(s2)
    print(res2)

    s3 = ["h", "e", "l", "l", "o"]
    solution3 = Solution3()
    res3 = solution3.reverseString(s3)
    print(res3)
