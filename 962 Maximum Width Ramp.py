#!/usr/bin/python3
"""
Given an array A of integers, a ramp is a tuple (i, j) for which i < j and
A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.



Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation:
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation:
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.


Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000
"""
from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        """
        Use stack? No, since require the furthest element rather than the closest
        Sort the values, keep its index
        Iterate the vlaues in increasing order, calcualte j - i
        Need to keep the smallest index
        """
        ret = -float("inf")
        V = [(a, i) for i, a in enumerate(A)]
        V.sort()
        min_idx = float("inf")
        for _, i in V:
            # V is sorted, guarantee a' > a
            ret = max(ret, i - min_idx)
            min_idx = min(min_idx, i)

        return max(ret, 0)
