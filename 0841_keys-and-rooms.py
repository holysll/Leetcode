# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-31 21:35
# software: PyCharm
"""
题目：钥匙和房间

有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。

在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。

最初，除 0 号房间外的其余所有房间都被锁住。

你可以自由地在房间之间来回走动。

如果能进入每个房间返回 true，否则返回 false。

示例 1：

输入: [[1],[2],[3],[]]
输出: true
解释:
我们从 0 号房间开始，拿到钥匙 1。
之后我们去 1 号房间，拿到钥匙 2。
然后我们去 2 号房间，拿到钥匙 3。
最后我们去了 3 号房间。
由于我们能够进入每个房间，我们返回 true。
示例 2：

输入：[[1,3],[3,0,1],[2],[0]]
输出：false
解释：我们不能进入 2 号房间。
提示：

1 <= rooms.length <= 1000
0 <= rooms[i].length <= 1000
所有房间中的钥匙数量总计不超过 3000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/keys-and-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 深度优先搜索
# 时间复杂度：O(n+m)，空间复杂度：O(n)
import collections


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        def dfs(x):
            visited.add(x)
            nonlocal num
            num += 1
            for i in rooms[x]:
                if i not in visited:
                    dfs(i)

        n = len(rooms)
        num = 0
        visited = set()
        dfs(0)
        return num == n


# 广度优先搜索
# 时间复杂度：O(n+m)，空间复杂度：O(n)
class Solution1(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        num = 0
        visited = {0}
        q = collections.deque([0])

        while q:
            x = q.popleft()
            num += 1
            for i in rooms[x]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)

        return num == n

if __name__ == '__main__':
    rooms = [[1, 3], [3, 0, 1], [2], [0]]
    solution = Solution()
    res = solution.canVisitAllRooms(rooms)
    print(res)

    solution1 = Solution1()
    res1 = solution1.canVisitAllRooms(rooms)
    print(res1)
