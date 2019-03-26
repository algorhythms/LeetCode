#!/usr/bin/python3
"""
Given an array A, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.



Example 1:

Input: [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]


Note:

2 <= A.length <= 30000
0 <= A[i] <= 10^6
It is guaranteed there is at least one way to partition A as described.
"""
from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        """
        max(left) <= min(right)

        similar to 2 in terms of keyboard stroke count 
        """
        n = len(A)
        MX = [-float('inf') for _ in range(n+1)]
        MI = [float('inf') for _ in range(n+1)]
        for i in range(n):
            MX[i+1] = max(M[i], A[i])
        for i in range(n-1, -1, -1):
            MI[i] = min(MI[i+1], A[i])

        for l in range(1, n+1):
            if MX[l] <= MI[l]:
                return l
        raise

    def partitionDisjoint_2(self, A: List[int]) -> int:
        """
        max(left) <= min(right)
        """
        MX = [0 for _ in A]
        MI = [0 for _ in A]
        MX[0] = A[0]
        MI[-1] = A[-1]
        n = len(A)
        for i in range(1, n):
            MX[i] = max(MX[i-1], A[i])
        for i in range(n-2, -1, -1):
            MI[i] = min(MI[i+1], A[i])

        for i in range(n-1):
            if MX[i] <= MI[i+1]:
                return i

        raise
