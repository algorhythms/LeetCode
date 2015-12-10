"""
Premium Question
Generation
https://leetcode.com/problems/strobogrammatic-number-iii/
"""
from collections import deque

__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.lst = ["11", "69", "88", "96", "00"]
        self.middle = ["0", "1", "8"]

    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        cnt = 0
        for l in xrange(len(low), len(high)+1):
            cnt += len(filter(lambda x: int(low) <= int(x) <= int(high), self.strobogrammatic(l)))

        return cnt

    # below methods from strobogrammatic number ii
    def strobogrammatic(self, n):
        ret = []
        self.build(n, deque(), ret)
        return ret

    def build(self, n, cur, ret):
        """
        build from inside
        """
        if n%2 == 1 and len(cur) == 0:
            for elt in self.middle:
                cur.append(elt)
                self.build(n, cur, ret)
                cur.pop()
        else:
            if len(cur) == n:
                ret.append("".join(cur))
                return
            for elt in self.lst:
                if not (elt == "00" and len(cur) == n-2):
                    cur.appendleft(elt[0])
                    cur.append(elt[1])
                    self.build(n, cur, ret)
                    cur.pop()
                    cur.popleft()