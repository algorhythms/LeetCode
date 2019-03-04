#!/usr/bin/python3
"""
Given a non-negative integer N, find the largest number that is less than or
equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair
of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        332
        322
        222
        fill 9
        299
        """
        digits = [int(e) for e in str(N)]
        pointer = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i - 1] > digits[i]:
                pointer = i
                digits[i - 1] -= 1

        for i in range(pointer, len(digits)):
            digits[i] = 9

        return int("".join(map(str, digits)))


if __name__ == "__main__":
    assert Solution().monotoneIncreasingDigits(10) == 9
    assert Solution().monotoneIncreasingDigits(332) == 299
