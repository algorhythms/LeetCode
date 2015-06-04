"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming
weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should
return 3.
"""
__author__ = 'Daniel'


class Solution:
    def hammingWeight(self, n):
        """
        /2 and %2
        """
        cnt = 0
        while n:
            cnt += n&1
            n >>= 1

        return cnt
