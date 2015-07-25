"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Stack Data Structure
"""
__author__ = 'Danyang'


class MinStack:
    def __init__(self):
        """
        algorithm: non_asc stack keeps the items of the normal stack if they are in non-ascending order
        normal stack: 5 4 3 5 4 3 2 1
        non-asc stack: 5 4 3 3 2 1

        when push: check whether in non-ascending order
        when pop: check whether in non-asc stack, if yes, pop it out from non-asc stack also

        if maintain the non_asc stack in this way, the non-ssc stack always keeps the non-ascending items of the normal
        stack
        :return:
        """
        self.stk = []
        self.non_asc = []

    def push(self, x):
        """

        :param x: int
        :return: int
        """
        self.stk.append(x)
        if len(self.non_asc) == 0 or x <= self.non_asc[-1]:  # rather than <
            self.non_asc.append(x)

    def pop(self):
        """

        :return: nothing
        """
        x = self.stk.pop()
        if x == self.non_asc[-1]:
            self.non_asc.pop()

    def top(self):
        """

        :return: int
        """
        return self.stk[-1]

    def getMin(self):
        """

        :return: int
        """
        return self.non_asc[-1]

