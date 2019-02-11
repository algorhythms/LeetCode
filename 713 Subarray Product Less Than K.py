#!/usr/bin/python3
"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all
the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
[2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less
than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        Two pointer
        Count attribute to the end
        """
        i = 0
        ret = 0
        p = 1
        for j in range(len(nums)):
            p *= nums[j]
            while p >= k and i <= j:
                p //= nums[i]
                i += 1

            ret += j - i + 1  # count attribute
            # if i > j, i can only be j + 1

        return ret
