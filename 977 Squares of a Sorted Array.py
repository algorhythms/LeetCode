#!/usr/bin/python3
"""
Given an array of integers A sorted in non-decreasing order, return an array of
the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """
        started from two ends
        """
        n = len(A)
        ret = deque()
        lo = 0
        hi = n
        while lo < hi:
            if A[lo] ** 2 < A[hi - 1] ** 2:
                ret.appendleft(A[hi - 1] ** 2)
                hi -= 1
            else:
                ret.appendleft(A[lo] ** 2)
                lo += 1

        return list(ret)
