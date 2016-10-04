"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 <= x < 10^n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 <= x < 100, excluding
[11,22,33,44,55,66,77,88,99])
"""
__author__ = 'Daniel'


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        Let F(i) be the number of numbers with unique digits of length i
        F(1) = 1 // special case
        F(i) = (10-1) * 9 * 8 * (10-i+1) // general case, 998
        (10-1) since the leading digit cannot be zero

        return sum F(i)
        :type n: int
        :rtype: int
        """
        ret = 1
        Fi = 1
        for i in xrange(n):
            Fi *= (10-i) if i != 0 else 9
            ret += Fi

        return ret
