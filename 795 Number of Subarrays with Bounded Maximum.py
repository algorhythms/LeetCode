#!/usr/bin/python3
"""
We are given an array A of positive integers, and two positive integers L and R
(L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of
the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1],
[3].
Note:

L, R  and A[i] will be an integer in the range [0, 10^9].
The length of A will be in the range of [1, 50000].
"""
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        """
        DP: Let F[i] be the num subarray with bounded max at A[i]
        if L <= A[i] <= R: F[i] = i - prev, where prev is previously invalid F[prev] = 0
        if A[i] > R: F[i] = 0
        if A[i] < L: F[i] = F[i-1]  # append itself to every array in F[i-1]

        memory optimization - one counter F is enough
        """
        F = 0
        ret = 0
        prev = -1
        for i, a in enumerate(A):
            if L <= a <= R:
                F = i - prev
                ret += F
            elif a > R:
                F = 0
                prev = i
            else:
                # F = F
                ret += F

        return ret

    def numSubarrayBoundedMax_error(self, A: List[int], L: int, R: int) -> int:
        """
        DP: Let F[i] be the num subarray with bounded max at A[i]
        if L <= A[i] <= R: F[i] = F[i-1] + 1  # append itself to every array in F[i-1] and one more itself
                           ^ ERROR
        if A[i] > R: F[i] = 0
        if A[i] < L: F[i] = F[i-1]  # append itself to every array in F[i-1]

        memory optimization - one counter F is enough
        """
        F = 0
        ret = 0
        for a in A:
            if L <= a <= R:
                F += 1  # error
                ret += F
            elif a > R:
                F = 0
            else:
                # F = F
                ret += F

        return ret
