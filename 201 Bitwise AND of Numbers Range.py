"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
__author__ = 'Daniel'


class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        Brute force O(N), which is suitable for all bit operations not just AND.

        Observation:
        After enumerating some example, we have the following observation:
        * The numbers \in [m, n] will enumerate all possible 0, 1 in bits starting from LSB except for left header of 1
        * Left header of 1's is will be result 

        left header
        :type m: int
        :type n: int
        :rtype: int
        """
        pos = 0
        while m != n:
            pos += 1
            m >>= 1
            n >>= 1

        return n << pos  # or m << pos

