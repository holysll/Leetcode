# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-11 20:38
# software: PyCharm
""""
题目：二叉树的层次遍历 II

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 广度搜索优先BFS
class Solution1(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.pop(0)  # 取队列头结点
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.insert(0, level)  # 插入到列表开头

        return res


# 深度搜索优先DFS
class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []

        def dfs(node, depth):
            if len(res) == depth:
                res.insert(0, [])  # 当一层遍历完，插入[]到开头
            res[-(depth + 1)].append(node.val)  # 将节点添加进[]
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


# 创建树
def createTree(root):
    if root == None:
        return root

    Root = TreeNode(root[0])
    nodeQueue = [Root]
    index = 1
    front = 0
    while index < len(root):
        node = nodeQueue[front]

        item = root[index]
        index += 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(root):
            break

        item = root[index]
        index += 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

        front += 1

    return Root

# 打印树
def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
    treeRoot = createTree(root)
    # printTree(treeRoot)
    solution1 = Solution1()
    res1 = solution1.levelOrderBottom(treeRoot)
    print(res1)
