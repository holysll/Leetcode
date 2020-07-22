# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-14 17:28
# software: PyCharm
"""
题目：二叉树中的最大路径和

给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 定义二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 官方递归解法
class Solution(object):
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def get_max(node):
            if not node:
                return 0

            # 递归计算左右节点的最大贡献值，并且要大于0
            left = max(get_max(node.left), 0)
            right = max(get_max(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右节点的最大贡献值
            max_path = node.val + left + right

            # 更新最大路径值
            self.maxSum = max(self.maxSum, max_path)

            # 返回节点的最大贡献值
            return node.val + max(left, right)

        get_max(root)
        return self.maxSum


# 大佬逻辑清晰解答
"""
思路：
最大路径和：根据当前节点的角色，路径和可分为两种情况：
    一：以当前节点为根节点
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    4.当前节点+左右子树    
    这四种情况的最大值即为以当前节点为根的最大路径和
    此最大值要和已经保存的最大值比较，得到整个树的最大路径值
    
    二：当前节点作为父节点的一个子节点
    和父节点连接的话则需取【单端的最大值】
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    这三种情况的最大值   
"""
import sys


class Solution1(object):
    res = -sys.maxsize - 1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue(root)
        return self.res

    def maxValue(self, node):
        if not node:
            return 0
        left_value = self.maxValue(node.left)
        right_value = self.maxValue(node.right)

        value1 = node.val
        value2 = node.val + left_value
        value3 = node.val + right_value
        value4 = node.val + left_value + right_value

        # 以此节点为根节点的最大值
        maxValue = max([value1, value2, value3, value4])

        # 当前遍历树的最大值
        self.res = max(maxValue, self.res)

        # 和父节点关联，去除情况4的最大值
        return max([value1, value2, value3])


# 递归，后续遍历
class Solution2(object):
    res = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            self.res = max(self.res, max(l, 0) + max(r, 0) + node.val)
            return max(l, r, 0) + node.val

        helper(root)
        return self.res


if __name__ == '__main__':
    solution = Solution()
    solution.maxPathSum()
