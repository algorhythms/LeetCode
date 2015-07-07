"""
Given an integer, write a function to determine if it is a power of two.
"""
__author__ = 'Daniel'


class Solution:
    def isPowerOfTwo(self, n):
        """
        Bit manipulation
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        return n & (n-1) == 0