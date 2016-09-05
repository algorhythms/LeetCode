"""
Premium Question
"""
from collections import deque

__author__ = 'Daniel'


class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.

        calls are being made to the system in chronological order.
        It is possible that several hits arrive roughly at the same time.
        What if the number of hits per second could be very large? Does your design scale?  # use counter
        """
        self.q = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.pop(timestamp)
        self.q.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        self.pop(timestamp)
        return len(self.q)

    def pop(self, timestamp):
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)