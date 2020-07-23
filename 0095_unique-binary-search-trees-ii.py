# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-21 21:50
# software: PyCharm
"""
题目：不同的二叉搜索树 II

给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

提示：

0 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages


# 定义一个二叉树的节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def sonTrees(start, end):
            if start > end:
                return [None,]

            allTrees = []
            for i in range(start, end+1): # 枚举可行根节点
                # 获得所有可能的左子树集合
                leftTrees = sonTrees(start, i-1)

                # 获得所有可行的右子树集合
                rightTrees = sonTrees(i+1, end)

                # 从左子树集合中选出一颗左子树，从右子树集合中选出一颗右子树，拼接到根节点上
                for left in leftTrees:
                    for right in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = left
                        currTree.right = right
                        allTrees.append(currTree)

            return allTrees

        return sonTrees(1, n) if n else []


class Solution2(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return list()

        d = dict()
        return self._generateTrees(1, n, d)

    def _generateTrees(self, left, right, d):
        if left > right:
            return [None]
        if (left, right) in d:
            return d[(left, right)]

        res = list()
        for i in range(left, right + 1):
            left_nodes = self._generateTrees(left, i-1, d)
            right_nodes = self._generateTrees(i+1, right, d)
            for left_node in left_nodes:
                for right_node in right_nodes:
                    root = TreeNode(i)
                    root.left = left_node
                    root.right = right_node
                    res.append(root)

        d[(left, right)] = res
        return res
