#!/usr/bin/python3
"""
Given an integer array, find three numbers whose product is maximum and output
the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24


Note:

The length of the given array will be in range [3,104] and all elements are in
the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of
32-bit signed integer.
"""
import heapq

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        heapq nlargest nsmallest
        """
        mxes = heapq.nlargest(3, nums)
        mns = heapq.nsmallest(3, nums)
        return max(
            mxes[0] * mxes[1] * mxes[2],
            mns[0] * mns[1] * mxes[0],
        )
