"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum
to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
import math

__author__ = 'Daniel'


class Solution(object):
    def numSquares(self, n):
        """
        DP
        :type n: int
        :rtype: int
        """
        F = [i for i in xrange(n+1)]
        for i in xrange(0, n+1):
            for j in xrange(1, int(math.sqrt(n-i))+1):
                if i+j*j <= n:
                    F[i+j*j] = min(F[i+j*j], F[i]+1)
                else:
                    break

        return F[n]

    def numSquares_TLE(self, n):
        """
        DP
        :type n: int
        :rtype: int
        """
        F = [i for i in xrange(n+1)]
        for i in xrange(1, n+1):
            for j in xrange(1, int(math.sqrt(i))+1):
                if i-j*j >= 0:
                    F[i] = min(F[i], F[i-j*j]+1)

        return F[n]


if __name__ == "__main__":
    print Solution().numSquares(13)