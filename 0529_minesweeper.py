# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-20 21:12
# software: PyCharm
"""
题目：扫雷游戏

让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

示例 1：

输入:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

示例 2：

输入:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

输出:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

注意：

输入矩阵的宽和高的范围为 [1,50]。
点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。
输入面板不会是游戏结束的状态（即有地雷已被挖出）。
简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minesweeper
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 适合新手的深度优先讲解
# https://space.bilibili.com/536702703
import collections


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        n = len(board)
        m = len(board[0])
        dic = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

        def search_around(x, y):
            count = 0
            for i, j in dic:
                if 0 <= x + i <= n - 1 and 0 <= y + j <= m - 1:
                    if board[x + i][y + j] == 'M':
                        count += 1
            return count

        def dfs(x, y):
            if x < 0 or x > n - 1 or y < 0 or y > m - 1:
                return
            if board[x][y] != "E":
                return
            count = search_around(x, y)
            if count != 0:
                board[x][y] = str(count)
                return
            else:
                board[x][y] = "B"
                for i, j in dic:
                    dfs(x + i, y + j)

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board
        else:
            dfs(click[0], click[1])
            return board


# 深度优先搜索DFS
class Solution1(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i, j = click
        m, n = len(board), len(board[0])
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 计算空白块周围的***
        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == "M":
                        res += 1
            return res

        def dfs(i, j):
            num = cal(i, j)
            if num > 0:
                board[i][j] = str(num)
                return
            board[i][j] = "B"
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0:
                        continue
                    p, q = i + x, j + y
                    if 0 <= p < m and 0 <= q < n and board[p][q] == "E":
                        dfs(p, q)

        dfs(i, j)
        return board


# 广度优先搜索BFS
class Solution2(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        i, j = click
        m, n = len(board), len(board[0])
        if board[i][j] == "M":
            board[i][j] = "X"
            return board

        # 计算空白块周围的***
        def cal(i, j):
            res = 0
            for x in [1, -1, 0]:
                for y in [1, -1, 0]:
                    if x == 0 and y == 0:
                        continue
                    if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == "M":
                        res += 1
            return res

        def bfs(i, j):
            queue = collections.deque([[i,j]])
            while queue:
                i, j = queue.pop()
                num = cal(i,j)
                if num > 0:
                    board[i][j] = str(num)
                    continue
                board[i][j] = "B"
                for x in [1, -1, 0]:
                    for y in [1, -1, 0]:
                        if x == 0 and y == 0:
                            continue
                        p, q = i + x, j + y
                        if p < 0 or p >= m or q < 0 or q >= n:
                            continue
                        if board[p][q] == "E":
                            queue.appendleft([p,q])
                            board[p][q] = "B"

        bfs(i, j)
        return board


if __name__ == '__main__':
    board = [
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ]
    click = [1, 2]
    solution = Solution()
    res = solution.updateBoard(board, click)
    print(res)

    board1 = [
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ]
    click1 = [1, 2]
    solution1 = Solution1()
    res1 = solution1.updateBoard(board1, click1)
    print(res1)

    board2 = [
        ['B', '1', 'E', '1', 'B'],
        ['B', '1', 'M', '1', 'B'],
        ['B', '1', '1', '1', 'B'],
        ['B', 'B', 'B', 'B', 'B']
    ]
    click2 = [1, 2]
    solution2 = Solution2()
    res2 = solution2.updateBoard(board2, click2)
    print(res2)
