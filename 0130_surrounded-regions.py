# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-11 15:52
# software: PyCharm
"""
题目：被围绕的区域

给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 深度优先搜索
class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


# 广度优先搜索
import collections


class Solution1(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        n, m = len(board), len(board[0])
        q = collections.deque()

        for i in range(n):
            if board[i][0] == "O":
                q.append((i, 0))
            if board[i][m - 1] == "O":
                q.append((i, m - 1))
        for j in range(m - 1):
            if board[0][j] == "O":
                q.append((0, j))
            if board[n - 1][j] == "O":
                q.append((n - 1, j))

        while q:
            x, y = q.popleft()
            board[x][y] = "A"
            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < n and 0 <= j < m and board[i][j] == "O":
                    q.append((i, j))

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"


# 利用map()函数
class Solution2(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                board[i][j] = "*"
                list(map(dfs, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))

        for i in range(m):
            list(map(dfs, (i, i), (0, n - 1)))

        for j in range(n):
            list(map(dfs, (0, m - 1), (j, j)))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "*":
                    board[i][j] = "O"


if __name__ == '__main__':
    matrix = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution = Solution()
    solution.solve(matrix)
    print(matrix)

    matrix1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution1 = Solution1()
    solution1.solve(matrix1)
    print(matrix1)

    matrix2 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    solution2 = Solution2()
    solution2.solve(matrix2)
    print(matrix2)
