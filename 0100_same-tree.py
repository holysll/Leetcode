# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-7 1:04
# software: PyCharm
"""
题目：相同的树

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 定义一个二叉树节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 深度优先搜索, 时间复杂度：O(min(m,n)),空间复杂度：O(min(m,n))
# 如果两个二叉树都为空，则两个二叉树相同
# 如果二叉树其中一个为空，那么这两个二叉树一定不相同
# 如果二叉树都不为空，先判断它们根节点是否相同，若不相同则这两个二叉树不同；
# 若不相同，继续判断两个二叉树的左右子树都相同
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 广度优先搜索，时间复杂度：O(min(m,n)),空间复杂度：O(min(m,n))
# 如果两个二叉树都为空，则两个二叉树相同
# 如果二叉树其中一个为空，那么这两个二叉树一定不相同
# 如果二叉树都不为空，从根节点开始广度优先搜索，利用队列分别存储二叉树的节点
import collections
class Solution1(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])

        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:  # 判断根节点
                return False
            if (not node1.left)^(not node2.left):
                return False
            if (not node1.right)^(not node2.right):
                return False
            if node1.left:
                queue1.append(node1.left)
            if node1.right:
                queue1.append(node1.right)
            if node2.left:
                queue2.append(node2.left)
            if node2.right:
                queue2.append(node2.right)

        return not queue1 and not queue2