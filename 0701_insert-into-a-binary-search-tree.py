# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-14 16:16
# software: PyCharm
"""
题目：二叉搜索树中的插入操作

给定二叉搜索树（BST）的根节点和要插入树的值，将值插入二叉搜索树。返回插入后二叉搜索树的根节点。保证原始二叉搜索树不存在新值。

注意，可能存在多种有效的插入方式，只要树在插入后保持为二叉搜索树即可。你可以返回任何有效的结果。

例如, 

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
你可以返回这个二叉搜索树:

         4
       /   \
      2     7
     / \   /
    1   3 5
或者这个树也是有效的:

         5
       /   \
      2     7
     / \
    1   3
         \
          4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-into-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages

# 定义二叉树节点
class TreeNode(object):
    def __init__(self, val = 0, left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val:  int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)

        if val > root.val:  # 插入的值大于根节点，则插入到右子树中
            root.right = self.insertIntoBST(root.right, val)
        else:  # 插入的值小于根节点，则插入到左子树中
            root.left = self.insertIntoBST(root.left, val)
        return root

# 迭代
class Solution1(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val:  int
        :rtype: TreeNode
        """
        node = root
        while node:
            if val > node.val:  # 插入到右子树
                if not node.right:  # 当右子树没有右子节点，则插入到右子树右节点
                    node.right = TreeNode(val)
                    return root
                else:  # 当右子树右节点存在，则指针指向该右子节点
                    node = node.right
            else:  # 插入左子树
                if not node.left:  # 当左子树没有左子节点，则插入到左子树右节点
                    node.left = TreeNode(val)
                    return root
                else:  # 当左子树左节点存在，则指针指向该左子节点
                    node = node.left
        return TreeNode(val)
