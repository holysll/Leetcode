# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-5 3:46
# software: PyCharm
"""
题目：
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Python packages
import sys
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个指针，pre 和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表
        while cur:
            # 记录当前节点的下一个节点
            temp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre 和 cur 节点都往后移一位
            pre = cur
            cur = temp
        return pre

def createList():
    head = ListNode(1)
    cur = head
    for i in range(1,6):
        cur.next = ListNode(i)
        cur = cur.next
    return head

def printList(head):
    cur = head
    while cur:
        print(cur.val, '-->', end='')
        cur = cur.next

    print('NULL')


if __name__ == '__main__':
    head = createList()
    solution = Solution()
    res = solution.reverseList(head)
    printList(res)