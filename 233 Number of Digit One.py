"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
__author__ = 'Daniel'


class Solution:
    def countDigitOne(self, n):
        """
        Count the 1 occurrences at the digit i, due to:
        1. the digits higher than the currently counting digits
        2. the digits lower than the currently counting digits

        Divide the question into smaller parts, count appearance at 1LSD, 2LSD, 3LSD respectively.
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0

        cnt = 0
        sig = 1
        while n/sig:
            temp = sig*10

            cur_digit = (n/sig)%10
            hi_digit = n/temp
            lo_digit = n%sig

            if cur_digit > 1:
                cnt += (hi_digit+1)*sig
            elif cur_digit == 1:
                cnt += hi_digit*sig + (lo_digit+1)
            else:
                cnt += hi_digit*sig

            sig = temp

        return cnt
