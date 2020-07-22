# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-10 20:42
# software: PyCharm
"""
题目：二叉树的前序遍历
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 定义二叉树节点
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归遍历，根-左-右
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


# 深度优先搜索解法DFS
class Solution1(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):  # 深度优先搜索，从上到下，从左到右
            if not root:
                return
            res.append(root.val)  # 根节点入栈
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res


# 迭代解法BFS
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []  # 存放结果
        stack = [root]  # 利用出栈确定根节点
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return res


# 模版解法，内存消耗严重
class Solution3(object):
    def preorderTraversal(self, root):
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
                root = root.left  # 遍历左子树
            root = stack.pop()  # 左子树遍历完毕
            root = root.right  # 遍历右子树
        return res


# 颜色标记法
"""
使用颜色标记节点的状态，新节点为白色，已访问的节点为灰色
如果遇到的节点为白色，则将其标记为灰色，然后将其右子节点、自身、左子点依次入栈。
如果遇到的节点为灰色，则将节点的值输出。
白色为0，灰色为1
"""


class Solution4(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [(0, root)]
        while stack:
            flag, node = stack.pop()
            if node is None: continue  # 空节点跳过
            if flag == 0:  # 前序的倒序记录，子节点标记为1，已经标记过 1 的父节点状态设置为0
                stack.append((0, node.right))
                stack.append((0, node.left))
                stack.append((1, node))
            else:  # 标记为1则输出
                res.append(node.val)
        return res

# 构建二叉树
def createTree(input_list):
    """
    :param input_list: 输入数列
    :return:
    """
    if not input_list or len(input_list) == 0:
        return []
    data = input_list.pop(0)
    if not data:
        return []
    root = TreeNode(data)
    root.left = createTree(input_list)
    root.right = createTree(input_list)
    return root

if __name__ == '__main__':
    my_input_list = list([1,None,2,3])
    root = createTree(my_input_list)
    solution = Solution()
    res = solution.preorderTraversal(root)
    print(res)

    solution1 = Solution1()
    res1 = solution1.preorderTraversal(root)
    print(res1)

    solution2 = Solution2()
    res2 = solution2.preorderTraversal(root)
    print(res2)

    solution3 = Solution3()
    res3 = solution3.preorderTraversal(root)
    print(res3)

    solution4 = Solution4()
    res4 = solution4.preorderTraversal(root)
    print(res4)
