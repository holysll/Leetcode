# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-13 17:10
# software: PyCharm
"""
题目：平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 定义二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归（深度优先搜索DFS）自底向上
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.right) + 1
            right = dfs(root.left) + 1

            if left == 0 or right == 0 or abs(left - right) > 1:
                return -1
            return max(left, right)

        return dfs(root) != -1


# 自顶而下
class Solution1(object):
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def maxDepth(root):
            if not root:
                return True, 0
            lf, lh = maxDepth(root.left)
            rf, rh = maxDepth(root.right)
            if lf and rf and abs(lh - rh) < 2:
                return True, max(lh, rh) + 1
            return False, max(lh, rh) + 1
        return maxDepth(root)[0]


def createTree(data):
    """
    创建二叉树
    :param data: List
    :return:
    """
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一个根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root


if __name__ == '__main__':
    nums = [3, 9, 20, None, None, 15, 7]
    root = createTree(nums)
    solution = Solution()
    res = solution.isBalanced(root)
    print(res)

    solution1 = Solution1()
    res1 = solution1.isBalanced(root)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.isBalanced(root)
    print(res2)
