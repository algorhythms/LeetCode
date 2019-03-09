#!/usr/bin/python3
"""
Given an unsorted array of integers, find the length of longest increasing
subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to
return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        LIS dp + binary search
        Patience sort
        F maintains a increasing array
        F[i] stores the position of A[j] in the F

        For easch position i, the F[i]_old > F[i]_new, but A[j_old] < A[j_new]

        """
        F = [float('inf') for _ in nums]
        l = 0
        for n in nums:
            i = bisect_left(F, n)  # consider equal elements [2, 2]
            F[i] = n
            l = max(l, i + 1)

        return l
