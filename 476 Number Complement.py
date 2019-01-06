#!/usr/bin/python3
"""
Given a positive integer, output its complement number. The complement strategy
is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
"""


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        msb = 0
        while num >> msb:
            msb += 1

        mask = (1 << msb) - 1
        return mask & ~num


if __name__ == "__main__":
    assert Solution().findComplement(5) == 2
