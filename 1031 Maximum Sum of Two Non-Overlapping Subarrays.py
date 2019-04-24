#!/usr/bin/python3
"""
Given an array A of non-negative integers, return the maximum sum of elements in
two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For
clarification, the L-length subarray could occur before or after the M-length
subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) +
(A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.


Example 1:
Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length
2.

Example 2:
Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
length 2.

Example 3:
Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with
length 3.

Note:
L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""
from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        """
        Prefix sum + Brute force O(N^2)
        two pointer i, j
        """
        n = len(A)
        F = [0 for _ in range(n + 1)]
        for i, a in enumerate(A):
            F[i+1] = F[i] + a

        ret = -float("inf")
        for l, m in ((L, M), (M, L)):
            for i in range(n + 1 - l):
                for j in range(i + l, n + 1 - m):  # upper needs +1 here 
                    cur = F[i + l] - F[i] + F[j + m] - F[j]
                    ret = max(ret, cur)

        return ret


if __name__ == "__main__":
    assert Solution().maxSumTwoNoOverlap([0,6,5,2,2,5,1,9,4], 1, 2) == 20
