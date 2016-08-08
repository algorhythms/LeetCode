"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""
__author__ = 'Daniel'


class Solution(object):
    def isPerfectSquare(self, num):
        """
        Debugging binary search
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        lo = 1
        hi = num/2 + 1
        while lo < hi:
            mid = (lo + hi) / 2
            midsq = mid**2
            if midsq == num:
                return True
            elif midsq < num:
                lo = mid + 1
            else:
                hi = mid

        return False
