"""
Premium Question
"""
from collections import deque

__author__ = 'Daniel'


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()

        return float(self.sum) / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)