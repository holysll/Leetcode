# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-25 14:27
# software: PyCharm
"""
题目：分割数组的最大值

给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。

注意:
数组长度 n 满足以下条件:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
示例:

输入:
nums = [7,2,5,10,8]
m = 2

输出:
18

解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-largest-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 动态规划
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        dp = [[10 ** 18] * (m + 1) for i in range(n + 1)]
        sub = [0]
        for num in nums:
            sub.append(sub[-1] + num)

        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j - 1], sub[i] - sub[k]))

        return dp[n][m]


# 二分查找 + 贪心
class Solution1(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # 检查二分的中点偏大还是偏小，决定迭代的方向
        def check(x):
            total, cnt = 0, 1  # total表示当前数组的和，cnt表示使用x会得到几个数组
            for num in nums:
                if total + num > x:  # 如果当前数组已经超过了x，停止这个数组
                    cnt += 1  # 得到数组数量+1
                    total = num  # 当前数组的和则会变为下一个数组的开头
                else:
                    total += num
            return cnt <= m  # 数组数量小于等于m，说明 mid 太大，二分查找取左边

        # 确定二分查找的范围
        left = max(nums)
        right = sum(nums)
        # 开始二分查找，当left等于right时终止查找，返回任意一个
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


# 优化
class Solution2(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= m:
            return max(nums)
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = low + (high - low) // 2
            if self.check(nums, m, mid):
                high = mid
            else:
                low = mid + 1
        return low

    def check(self, nums, m, mid):
        total = 0
        for num in nums:
            # 如果子序和 + 下一个数 超过分组阈值，则m-1
            if total + num > mid:
                m -= 1
                if m <= 0:
                    return False
                # 下一个数 在下一个分组里面
                total = num
            else:
                # 否则的话，继续加
                total += num
        return True


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    solution = Solution()
    res = solution.splitArray(nums, m)
    print(res)

    solution1 = Solution1()
    res1 = solution1.splitArray(nums, m)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.splitArray(nums, m)
    print(res2)
