#!/usr/bin/python3
"""
Given an unsorted array of integers, find the number of longest increasing
subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and
[1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and
there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is
guaranteed to be fit in 32-bit signed int.
"""
from typing import List


class LenCnt:
    def __init__(self, l, c):
        self.l = l
        self.c = c

    def __repr__(self):
        return repr((self.l, self.c))


class Solution:
    def findNumberOfLIS(self, A: List[int]) -> int:
        """
        Two pass - 1st pass find the LIS, 2nd pass find the number
        Let F[i] be the length of LIS ended at A[i]
        """
        if not A:
            return 0

        n = len(A)
        F = [LenCnt(l=1, c=1) for _ in A]
        mx = LenCnt(l=1, c=1)
        for i in range(1, n):
            for j in range(i):
                if A[i] > A[j]:
                    if F[i].l < F[j].l + 1:
                        F[i].l = F[j].l + 1
                        F[i].c = F[j].c
                    elif F[i].l == F[j].l + 1:
                        F[i].c += F[j].c

            if F[i].l > mx.l:
                # mx = F[i]  error, need deep copy
                mx.l = F[i].l
                mx.c = F[i].c
            elif F[i].l == mx.l:
                mx.c += F[i].c

        return mx.c


if __name__ == "__main__":
    assert Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]) == 27
    assert Solution().findNumberOfLIS([1, 3, 5, 4, 7]) == 2
    assert Solution().findNumberOfLIS([2, 2, 2, 2, 2]) == 5
