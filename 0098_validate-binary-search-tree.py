# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-14 3:12
# software: PyCharm
"""
题目：验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages


# 定义二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归解法
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            if not helper(node.right, node.val, upper):
                return False
            if not helper(node.left, lower, node.val):
                return False
            return True

        return helper(root)

# 中序遍历（左-根-右），得到的序列是是升序结果即可
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        inorder = float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()  # 左子树遍历完毕
            if root.val <= inorder:  # 中序遍历得到的节点值小于等于前一个inorder，则非二叉搜索树
                return False
            inorder = root.val
            root = root.right

        return True

# 递归解法，pythonic代码
class Solution2(object):
    def isValidBST(self, root):
        """
        :param root: TreeNode
        :return: bool
        """
        def BFS(node, left, right):
            """
            :param root: 节点
            :param left: 下界
            :param right: 上界
            :return: bool
            """
            if not node:
                return True
            if left < node.val < right:
                return BFS(node.left, left, node.val) and BFS(node.right, node.val, right)
            else:
                return False

        return BFS(root, -float('inf'), float('inf'))