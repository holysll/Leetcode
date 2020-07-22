# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-13 15:59
# software: PyCharm
"""
题目： 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 定义二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归（深度优先搜索DFS）
# 时间复杂度为 O(N)，空间复杂度 O(log(N))
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# 迭代（深度优先搜索DFS），利用栈
class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        stack = [(1, root)]
        depth = 0
        while stack:
            h, node = stack.pop()
            depth = max(depth, h)
            if node.left:
                stack.append((h + 1, node.left))
            if node.right:
                stack.append((h + 1, node.right))
        return depth


# 迭代（广度优先搜索BFS），队列
class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [(1, root)]  # 添加一个层数depth参数
        while queue:
            depth, root = queue.pop(0)
            if root.left:
                queue.append((depth + 1, root.left))
            if root.right:
                queue.append((depth + 1, root.right))
        return depth


# 分治法
class Solution3(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left > right:
            return left + 1
        else:
            return right + 1


if __name__ == '__main__':
    solution = Solution()
    solution.maxDepth()
