# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-9 21:37
# software: PyCharm
"""
题目：恢复二叉搜索树

二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 定义一个二叉树节点
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归+深度优先搜索
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        Trees = lambda x: [] if not x else Trees(x.left) + [x] + Trees(x.right)
        node = Trees(root)
        s = sorted(node, key=lambda x: x.val)
        tmp = [node[i] for i in range(len(node)) if node[i] != s[i]]
        tmp[0].val, tmp[1].val = tmp[1].val, tmp[0].val


# 中序遍历
class Solution1(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root: return

            # 遍历左子树
            inorder(root.left)

            nonlocal pre, nodes
            # 记录当前的逆序
            if pre and pre.val > root.val:
                nodes.append(pre)
                nodes.append(root)
            pre = root

            # 遍历左子树
            inorder(root.right)

        pre = None
        nodes = []
        inorder(root)
        if len(nodes) == 2:
            i, j = 0, 1
        elif len(nodes) == 4:
            i, j = 0, 3
        else:
            return

        nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
        return
