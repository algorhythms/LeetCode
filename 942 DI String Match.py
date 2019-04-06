#!/usr/bin/python3
"""
Given a string S that only contains "I" (increase) or "D" (decrease), let N =
S.length.

Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

If S[i] == "I", then A[i] < A[i+1]
If S[i] == "D", then A[i] > A[i+1]


Example 1:

Input: "IDID"
Output: [0,4,1,3,2]
Example 2:

Input: "III"
Output: [0,1,2,3]
Example 3:

Input: "DDI"
Output: [3,2,0,1]


Note:

1 <= S.length <= 10000
S only contains characters "I" or "D".
"""
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        """
        Looking at prev rather than cur
            If "I", then put smallest as prev. Increase from the min
            If "D", then put the largest as prev. Decrese from the max
        """
        mini, maxa = 0, len(S)
        ret = []
        for c in S:
            if c == "I":
                ret.append(mini)
                mini += 1
            else:  # "D"
                ret.append(maxa)
                maxa -= 1

        ret.append(mini)
        return ret

    def diStringMatchErrror(self, S: str) -> List[int]:
        """
        start with 0, then add the min up to 0

        errror since cannot repeat
        """
        ret = [0]
        for c in S:
            if c == "I":
                ret.append(ret[-1] + 1)
            else:
                ret.append(ret[-1] -1)
        mn = min(ret)
        return [
            e - mn
            for e in ret
        ]
