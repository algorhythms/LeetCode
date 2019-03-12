#!/usr/bin/python3
"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to
the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
after one shift on A. Return True if and only if A can become B after some
number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        """
        brute force O(n^2), shift and compare but short circuit
        """
        if len(A) != len(B):
            return False

        if not A and not B:
            return True

        for i in range(1, len(A)):
            for j in range(len(B)):
                if A[(i + j) % len(A)] != B[j]:
                    break
            else:
                return True

        return False
