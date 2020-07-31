# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-31 15:28
# software: PyCharm
"""
题目：最大数

给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 官方解答
class LargeNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        largest_num = ''.join(sorted(map(str, nums), key=LargeNumKey))
        return '0' if largest_num[0] == '0' else largest_num


# 字符串转换为浮点数排序
def compare(x):
    if x == 0:
        return 0
    m = 0
    n = x
    while x >= 1:
        x = x / 10
        m += 1
    return n / float(10 ** m - 1)


class Solution1(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        s = sorted(nums, key=compare, reverse=True)
        if s[0] == 0:
            return '0'
        return "".join([str(i) for i in s])


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    solution = Solution()
    res = solution.largestNumber(nums)
    print(res)

    solution1 = Solution1()
    res1 = solution1.largestNumber(nums)
    print(res1)

