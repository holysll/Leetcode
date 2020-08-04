# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-4 2:32
# software: PyCharm
"""
题目：课程表

你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]

给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。

提示：

输入的先决条件是由 边缘列表 表示的图形，而不是 邻接矩阵 。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
1 <= numCourses <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 拓扑排序经典问题--图
from collections import defaultdict,deque

# 深度优先搜索
# 时间复杂度：O(n+m)，空间复杂度：O(n+m)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(list)
        visited = [0] * numCourses
        res = list()
        valid = True

        for item in prerequisites:
            edges[item[1]].append(item[0])

        def dfs(x):
            nonlocal valid
            visited[x] = 1
            for v in edges[x]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[x] = 2
            res.append(x)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


# 广度优先搜索
# 时间复杂度：O(n+m)，空间复杂度：O(n+m)
class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = defaultdict(list)
        indeg = [0] * numCourses

        for item in prerequisites:
            edges[item[1]].append(item[0])
            indeg[item[0]] += 1

        q = deque([x for x in range(numCourses) if indeg[x] == 0])
        visited = 0

        while q:
            visited += 1
            i = q.popleft()
            for v in edges[i]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses


if __name__ == '__main__':
    numCourses, prerequisites = 2, [[1, 0], [0, 1]]
    solution = Solution()
    res = solution.canFinish(numCourses, prerequisites)
    print(res)

    solution1 = Solution1()
    res1 = solution1.canFinish(numCourses, prerequisites)
    print(res1)