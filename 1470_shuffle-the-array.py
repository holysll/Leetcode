# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-3 22:22
# software: PyCharm
"""
题目：重新排列数组

给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7]
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]

提示：

1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shuffle-the-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 自己写的
# 时间复杂度O(N^2)，空间复杂度O(N)
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            for j in range(i + n, len(nums)):
                if j - i == n:
                    res.append(nums[i])
                    res.append(nums[j])
        return res


# 利用栈
# 时间复杂度O(N)，空间复杂度O(N)
class Solution1(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i + n])
        return res


# 双指针
class Solution2(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        i, j = 0, n
        res = []
        while i < n:
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        return res


# 插入列表
class Solution3(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        new_nums = nums[0:n]
        for i in range(n):
            new_nums.insert(2 * i + 1, nums[i + n])
        return new_nums


# 插入列表
class Solution4(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n):
            res.extend(nums[i::n])
        return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 3, 2, 1]
    n = 4
    solution = Solution()
    res = solution.shuffle(nums, n)
    print(res)

    solution1 = Solution1()
    res1 = solution1.shuffle(nums, n)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.shuffle(nums, n)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.shuffle(nums, n)
    print(res3)

    solution4 = Solution4()
    res4 = solution4.shuffle(nums, n)
    print(res4)
