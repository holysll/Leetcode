# !/usr/bin/env python
# -*- coding:utf-8 -*-
# some description
# author: holysll
# datetime: 2020-7-30 13:30
# software: PyCharm
"""
题目：用队列实现栈

使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空

注意:

你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-stack-using-queues
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Python packages

# 单队列(list or 一维数组)实现
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        length = len(self.q)
        while length > 1:
            self.q.append(self.q.pop(0))  # 反转前n-1个元素，栈顶元素始终保留在队首
            length -= 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not bool(self.q)


# 使用双端队列deque
from collections import deque
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        length = len(self.q)
        self.q.append(x)
        for i in range(length):
            self.q.append(self.q.popleft())


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.popleft()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0
