#!/usr/bin/python3
"""
Given a number N, return a string consisting of "0"s and "1"s that represents
its value in base -2 (negative two).

The returned string must have no leading zeroes, unless the string is "0".



Example 1:

Input: 2
Output: "110"
Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
Example 2:

Input: 3
Output: "111"
Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
Example 3:

Input: 4
Output: "100"
Explantion: (-2) ^ 2 = 4


Note:
0 <= N <= 10^9
"""
from collections import deque


class Solution:
    def baseNeg2(self, N: int) -> str:
        """
        % -2, // -2 ? not really

        alternating


        3
        (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0, LSB set
        minus reminder, divide by -2
        (-2) ^ 1 + (-2) ^ 0, LSB set
        minus reminder, divide by -2
        (-2) ^ 0, LSB set

        4
        (-2) ^ 2 + 0 ^ 1 + 0 ^ 0, LSB not set
        minus reminder, divide by -2
        (-2) ^ 1 + 0 ^ 0, LSB not set
        minus reminder, divide by -2
        (-2) ^ 0, LSB set
        """
        ret = deque()
        while N != 0:
            r = N % 2  # r is the range of 0 and 2
            ret.appendleft(r)
            N -= r
            N //= -2

        return "".join(map(str, ret)) or "0"


if __name__ == "__main__":
    assert Solution().baseNeg2(3) == "111"
    assert Solution().baseNeg2(4) == "100"
