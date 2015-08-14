"""
Premium Question
"""
from math import sqrt

__author__ = 'Daniel'


class Solution:
    def getFactors(self, n):
        """

        :type n: int
        :rtype: list[list[int]]
        """
        ret = []
        self.dfs_TLE(n, [], ret)
        return ret

    def dfs_TLE(self, n, cur, ret):
        if n == 1 and cur and len(cur) >= 2:
            ret.append(list(cur))

        if cur:
            start = cur[-1]
        else:
            start = 2

        for i in xrange(start, int(sqrt(n+1))):
            if n%i == 0:
                cur.append(i)
                self.dfs_TLE(n/i, cur, ret)
                cur.pop()

if __name__ == "__main__":
    print Solution().getFactors(8)