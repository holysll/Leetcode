# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-27 22:16
# software: PyCharm
"""
题目：重新安排行程

给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reconstruct-itinerary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
import collections


# 深度搜索+回溯
import heapq


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)  # 邻接表
        for k, v in tickets:
            d[k] += [v]
        # print(d)

        for i in d:
            d[i].sort()  # 邻接表根据values排序

        res = []

        def dfs(x):
            while d[x]:
                dfs(d[x].pop(0))
            res.insert(0, x)  # 放在最前面

        dfs("JFK")
        return res

# 利用深度优先+最小堆
class Solution1(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)
        for k, v in tickets:
            d[k].append(v)
        for key in d:
            heapq.heapify(d[key])

        res = []
        def dfs(x):
            while d[x]:
                tmp = heapq.heappop(d[x])
                dfs(tmp)
            res.append(x)

        dfs("JFK")
        return res[::-1]

if __name__ == '__main__':
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    solution = Solution()
    res = solution.findItinerary(tickets)
    print(res)

    solution1 = Solution1()
    res1 = solution1.findItinerary(tickets)
    print(res1)
