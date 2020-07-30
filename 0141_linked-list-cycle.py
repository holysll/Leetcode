# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-29 20:57
# software: PyCharm
"""
题目：环形链表

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages


# 定义一个单链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 用一个set数据结构存储每个节点地址
# 时间复杂度O(n*1)，空间复杂度O(n)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        a = set()
        while head:
            if head in a:
                return True
            a.add(head)
            head = head.next
        return False


# 哈希表（字典）
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1
            head = head.next
        return False


# 快慢指针
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

