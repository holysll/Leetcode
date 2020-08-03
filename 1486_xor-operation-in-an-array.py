# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-3 23:30
# software: PyCharm
"""
题目：数组异或操作

给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。

示例 1：

输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。
示例 2：

输入：n = 4, start = 3
输出：8
解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.
示例 3：

输入：n = 1, start = 7
输出：7
示例 4：

输入：n = 10, start = 5
输出：2

提示：

1 <= n <= 1000
0 <= start <= 1000
n == nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xor-operation-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages

# 暴力求解
# 时间复杂度O(N)，空间复杂度O(1)
import functools


class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        res = start
        for i in range(1, n):
            res ^= start + i * 2
        return res


# 高级函数reduce
from functools import reduce


class Solution1(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, [start + 2 * i for i in range(n)])


# 归纳方法，每四个数循环，时间复杂度O(1)
class Solution2(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        if (start & 3) < 2:
            if (n & 1) == 0:
                return n & 3
            else:
                return start + 2 * n - 3 + (n & 3)
        else:
            if (n & 1) == 0:
                return (start + (n - 1) * 2) ^ (start - 2 + (n & 3))
            else:
                return start + 1 - (n & 3)


if __name__ == '__main__':
    n = 5
    start = 0
    solution = Solution()
    res = solution.xorOperation(n, start)
    print(res)

    solution1 = Solution1()
    res1 = solution1.xorOperation(n, start)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.xorOperation(n, start)
    print(res2)
