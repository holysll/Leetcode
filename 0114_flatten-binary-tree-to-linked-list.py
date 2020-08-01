# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-2 2:38
# software: PyCharm
"""
题目：二叉树展开为链表

给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# import sys
#
# sys.setrecursionlimit(100)  # 最大递归次数


# 定义一个二叉树节点
class TreeNode(object):
    def __init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 前序遍历（递归）, 根-左-右
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        preorderList = list()

        def preorderTraversal(root):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        for i in range(1, len(preorderList)):
            pre, cur = preorderList[i - 1], preorderList[i]
            pre.left = None
            pre.right = cur


# 前序遍历（迭代）, 根-左-右
# 时间复杂度O(n)，空间复杂度O(n)
class Solution1(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        preorderList = []
        stack = []
        node = root

        while node or stack:
            while node:
                preorderList.append(node)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        for i in range(1, len(preorderList)):
            pre, cur = preorderList[i - 1], preorderList[i]
            pre.left = None
            pre.right = cur


# 前序遍历和展开同步进行
# 时间复杂度O(n)，空间复杂度O(n)
class Solution2(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        pre = None

        while stack:
            cur = stack.pop()
            if pre:
                pre.left = None
                pre.right = cur
            left, right = cur.left, cur.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            pre = cur


# 寻找前驱节点
# 时间复杂度O(n)，空间复杂度O(1)
class Solution3(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pre = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
