#!/usr/bin/python3
"""
Given a string S and a character C, return an array of integers representing the
shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        """
        get the sorted indexes of C
        """
        idx = [
            i
            for i in range(len(S))
            if S[i] == C
        ]
        idx = [-float("inf")] + idx + [float("inf")]
        ret = []
        i = 0
        for j in range(len(S)):
            while not idx[i] <= j < idx[i+1]:
                i += 1

            ret.append(min(j - idx[i], idx[i+1] - j))

        return ret
