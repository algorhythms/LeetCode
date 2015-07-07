"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty
operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque
(double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
__author__ = 'Daniel'


class Queue:
    def __init__(self):
        self.in_stk = []
        self.out_stk = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stk.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        self.out_stk.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        return self.out_stk[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.out_stk and not self.in_stk