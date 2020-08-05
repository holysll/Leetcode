# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-8-5 14:07
# software: PyCharm
"""
题目：打家劫舍 III

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 定义一个二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def func(root):
            if not root:
                return 0, 0  # 偷，不偷
            left = func(root.left)
            right = func(root.right)
            # 偷当前节点，则左右子树都不能偷
            v1 = root.val + left[1] + right[1]
            # 不偷当前节点，则取左右子树中的最大值
            v2 = max(left) + max(right)
            return v1, v2
        return max(func(root))


# 深度优先
"""
解题思路
每个节点都设置：[偷, 不偷]

每一个节点的偷值都是：左侧子节点的不偷值 + 右侧子节点的不偷值 + 该节点的值
每一个节点的不偷值都是： 左侧子节点的最大值 + 右侧子节点的最大值
"""
class Solution1(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a = self.dfs(root)
        return max(a[0], a[1])

    # 参数为root节点，dfs方法输出一个二维数组，root节点[偷，不偷]
    def dfs(self, root):
        if not root:
            return [0, 0]
        left = self.dfs(root.left)  # left是一个二维数组，root左侧子节点的[偷，不偷]
        right = self.dfs(root.right)  # right是一个二维数组，root右侧子节点的[偷，不偷]
        rob_value = left[1] + right[1] + root.val  # root的偷值
        unrob_value = max(left[0], left[1]) + max(right[0], right[1])  # root不偷值
        return [rob_value, unrob_value]
