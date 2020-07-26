# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-26 15:58
# software: PyCharm
"""
题目：矩阵中的最长递增路径

给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
输出: 4
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
输出: 4
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages


# 深度优先搜索+记忆化
import functools


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        store = [[None] * n for i in range(m)]
        res = 0  # 存储max路径值

        def search_nearby(i, j):
            nonlocal res
            compare = []  # 存储可以比较的候选人

            # 上
            if i != 0 and matrix[i - 1][j] > matrix[i][j]:  # 上边存在且上边的数小于当前数
                if store[i - 1][j]:
                    compare.append(store[i - 1][j])
                else:
                    compare.append(search_nearby(i - 1, j))
            # 下
            if i != m - 1 and matrix[i + 1][j] > matrix[i][j]:  # 下边存在且下边的数小于当前数
                if store[i + 1][j]:
                    compare.append(store[i + 1][j])
                else:
                    compare.append(search_nearby(i + 1, j))
            # 左
            if j != 0 and matrix[i][j - 1] > matrix[i][j]:  # 左边存在且左边的数小于当前数
                if store[i][j - 1]:
                    compare.append(store[i][j - 1])
                else:
                    compare.append(search_nearby(i, j - 1))
            # 右
            if j != n - 1 and matrix[i][j + 1] > matrix[i][j]:  # 右边存在且右边的数小于当前数
                if store[i][j + 1]:
                    compare.append(store[i][j + 1])
                else:
                    compare.append(search_nearby(i, j + 1))

            if compare:  # 路径+1
                store[i][j] = max(compare) + 1
            else:  # 如果没有compare这说明是一个很小的数，是一个起始点，能组成的长度只有1
                store[i][j] = 1

            res = max(res, store[i][j])
            return store[i][j]

        for i in range(m):
            for j in range(n):
                if not store[i][j]:
                    search_nearby(i, j)

        return res


from functools import lru_cache


# 深度优先遍历DFS
class Solution1(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        @lru_cache(maxsize=None)  # 这里使用LRU缓存，设置为不限制缓存大小
        def DFS(i, j):
            best = 1
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                m, n = x + i, y + j
                if 0 <= m < rows and 0 <= n < cols and matrix[m][n] > matrix[i][j]:
                    best = max(best, DFS(m, n) + 1)
            return best

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        for i in range(rows):
            for j in range(cols):
                res = max(res, DFS(i, j))
        return res

# 排序+动态规划
class Solution2(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[1 for i in range(n)] for j in range(m)]
        numsSort = sorted(sum([[(matrix[i][j], i, j) for j in range(n)] for i in range(m)], []))
        for i, j, k in numsSort:
            dp[j][k] = 1 + max(
                dp[j - 1][k] if j and matrix[j - 1][k] < i else 0,
                dp[j][k - 1] if k and matrix[j][k - 1] < i else 0,
                dp[j + 1][k] if j != m - 1 and matrix[j + 1][k] < i else 0,
                dp[j][k + 1] if k != n - 1  and matrix[j][k + 1] < i else 0
            )
        return max(sum(dp, []))


if __name__ == '__main__':
    nums = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    solution = Solution()
    res = solution.longestIncreasingPath(nums)
    print(res)

    solution1 = Solution1()
    res1 = solution1.longestIncreasingPath(nums)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.longestIncreasingPath(nums)
    print(res2)
