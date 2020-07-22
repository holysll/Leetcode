# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-10 23:16
# software: PyCharm
"""
题目： 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages


# 定义二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 深度优先搜索DFS
class Solution1(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):  # 深度优先搜索，从左-根节点-右
            if not root:
                return
            dfs(root.left)
            res.append(root.val)  # 根节点入栈
            dfs(root.right)
        dfs(root)
        return res

# 模版解法
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left  # 遍历左子树
            root = stack.pop()  # 左子树遍历完毕
            res.append(root.val)  # 将节点加入列表
            root = root.right  # 遍历右子树
        return res


# 颜色标记法
class Solution3(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [(0, root)]
        while stack:  # 前序的中序记录，子节点标记为1，已经标过1的父节点状态置为0
            flag, node = stack.pop()
            if node is None: continue  # 空节点跳过
            if flag == 0:
                stack.append((0, node.right))
                stack.append((1, node))
                stack.append((0, node.left))
            else:  # 标记为1则输出
                res.append(node.val)
        return res

if __name__ == '__main__':
    root = TreeNode(3)
    solution1 = Solution1()
    solution1.inorderTraversal(root)