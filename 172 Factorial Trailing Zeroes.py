"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
__author__ = 'Daniel'


class Solution:
    def trailingZeroes(self, n):
        """
        10 = 5*2
        Number of 2's > number of 5's, thus count the number of 5 in the factors of n

        Notice the special case of 25, which consists of two 5's

        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n /= 5
            cnt += n

        return cnt
