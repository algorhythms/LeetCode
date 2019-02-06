#!/usr/bin/python3
"""
Given a sorted array consisting of only integers where every element appears
twice except for one element which appears once. Find this single element that
appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""
from typing import List
from bisect import bisect_right


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        sorted array

        binary search with checking mid odd/even
        """
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if (
                mid % 2 == 0 and mid + 1 < hi and nums[mid] == nums[mid + 1]
            ) or (
                mid % 2 == 1 and mid - 1 >= lo and nums[mid] == nums[mid - 1]
            ):
                # to make the target is on the right
                # when mid even, mid and mid + 1 form a pair; there are odd number of elements on the right
                # when mid odd, mid and mid - 1 form a pair; there are odd number of elements on the right
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]


    def singleNonDuplicate_error(self, nums: List[int]) -> int:
        """
        sorted array

        consider the expected arry with no exception. The index of each element
        should be in the expected position
        binary search, compare the searched index and expected index
        """
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            idx = bisect_right(nums, nums[mid], lo, hi)
            if idx <= mid:
                hi = mid - 1
            else:
                lo = mid

        return nums[hi - 1]


    def singleNonDuplicate_xor(self, nums: List[int]) -> int:
        """
        XOR O(n)
        """
        ret = nums[0]
        for e in nums[1:]:
            ret ^= e
        return ret
