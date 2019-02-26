#!/usr/bin/python3
"""
Given a positive integer, check whether it has alternating bits: namely, if two
adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = None
        while n:
            cur = n & 1
            # `if last` is error
            if last is not None and last ^ cur == 0:
                return False
            last = cur
            n >>= 1

        return True


if __name__ == "__main__":
    assert Solution().hasAlternatingBits(5) == True
    assert Solution().hasAlternatingBits(7) == False
