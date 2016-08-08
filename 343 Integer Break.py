"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those
integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
__author__ = 'Daniel'


class Solution(object):
    def integerBreak(self, n):
        """
        First visualize the breakdown process into a search tree. The search tree dynamic programming
        Dynamic programming
        Let F[i] be the max product of summation breakdown integers of number i
        For each operands of the plus sign, there are choices of break it or not; thus we have for cases
        F[i] = max(
            F[j] * F[i-j],
            j * F[i-j],
            F[j] * (i-j),
            j * (i-j),
            for j in [1, i)
        ) if break down i
        :type n: int
        :rtype: int
        """
        F = [None for _ in xrange(n+1)]
        F[1] = 1
        for i in xrange(2, n+1):
            F[i] = max(
                max(F[j] * F[i-j], j * F[i-j], F[j] * (i-j), j * (i-j))
                for j in xrange(1, i/2)
            )

        return F[n]
