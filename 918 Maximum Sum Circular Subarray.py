#!/usr/bin/python3
"""
Given a circular array C of integers represented by A, find the maximum possible
sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of
the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] =
C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most
once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist
i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""
from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        Kadane's Algorithm
        Two cases:
        1. normal max subarray within A
        2. circular one, that both A[0] and A[n-1] is included
        (A0 + A1 + .. + Ai) + (Aj + ... + An-1)
        = sum(A) - (Ai+1 + ... + Aj-1)
        """
        ret1 = self.max_subarray(A)
        ret2 = sum(A) + self.max_subarray([-a for a in A[1:-1]])  # max negative (-1)
        return max(ret1, ret2)

    def max_subarray(self, A) -> int:
        """
        dp[i] = A[i] + max(dp[i-1],0)
        """
        mx = -float('inf')
        cur = 0
        for a in A:
            cur = a + max(cur, 0)  # RHS cur is the prev
            mx = max(mx, cur)
        return mx

    def maxSubarraySumCircular_error(self, A: List[int]) -> int:
        """
        keep a cur_sum with index, when negative, go back to 0
        """
        cur = [0, None]
        mx = -float('inf')
        i = 0
        j = 0
        n = len(A)
        while i < n:
            cur[0] += A[i]
            cur[1] = i
            mx = max(mx, cur[0])
            j = i + 1
            while cur[0] >= 0 and j < i + n:
                cur[0] += A[j % n]
                mx = max(mx, cur[0])
                j += 1

            i = j

        return mx
