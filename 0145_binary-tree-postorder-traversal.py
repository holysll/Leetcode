# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-10 23:39
# software: PyCharm
"""
题目：二叉树的后序遍历

给定一个二叉树，返回它的后序遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages


# 定义一个二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 用DFS深度优先搜索
class Solution1(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root):  # 深度优先搜索，从下到上，从左到右
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)  # 根节点入栈
        dfs(root)
        return res

# 模版解法，将前序遍历结果倒序输出
class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)  # 将根节点加入列表
                stack.append(root)
                root = root.right  # 遍历右子树
            root = stack.pop()  # 右子树遍历完毕
            root = root.left  # 遍历左子树
        return res[::-1]


# 颜色标记法(居然超时了)
class Solution3(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [(0, root)]
        while stack:
            flag, node = stack.pop()
            if node is None: continue  # 空节点继续
            if flag == 0:
                # 后序的中序记录，子节点标记为1，已经标记过1的父节点状态置为0
                stack.append((0, node))
                stack.append((0, node.left))
                stack.append((1, node.right))
            else:  # 标记为1则输出
                res.append(node.val)
        return res

if __name__ == '__main__':
    root = TreeNode(3)
    solution1 = Solution1()
    solution1.postorderTraversal(root)