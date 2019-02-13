#!/usr/bin/python3
"""
Given an integer array, you need to find one continuous subarray that if you
only sort this subarray in ascending order, then the whole array will be sorted
in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
whole array sorted in ascending order.

Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """
        Sorted at both ends
        Then search for the two ends by nums[i+1] > nums[i] on the left side
        (right side similar)

        Problem: may over-include, consider  1 2 5 9 4 6 ...
        need to shrink from 1 2 5 9 to 1 2 according to min value

        nums[lo - 1] <= min && max <= nums[hi + 1]
        """
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi and nums[lo] <= nums[lo + 1]:
            lo += 1

        while lo < hi and nums[hi - 1] <= nums[hi]:
            hi -= 1

        if hi <= lo:
            return 0

        mini = float('inf')
        maxa = -float('inf')
        for i in range(lo, hi + 1):
            mini = min(mini, nums[i])
            maxa = max(maxa, nums[i])

        while lo - 1 >= 0 and nums[lo - 1] > mini:
            lo -= 1
        while hi + 1 < n and nums[hi + 1] < maxa:
            hi += 1

        return hi - lo + 1

    def findUnsortedSubarray_sort(self, nums: List[int]) -> int:
        """
        Brute force sort and compare O(n lgn)
        """
        expected = list(sorted(nums))
        i = 0
        while i < len(nums) and nums[i] == expected[i]:
            i += 1

        j = len(nums) - 1
        while j >= i and nums[j] == expected[j]:
            j -= 1

        return j - i + 1


if __name__ == "__main__":
    assert Solution().findUnsortedSubarray([2, 1]) == 2
    assert Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
