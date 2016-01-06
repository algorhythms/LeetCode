# -*- coding: utf-8 -*-
"""
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum
≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""
__author__ = 'Daniel'
import sys


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        Brute force: O(n^2)
        two pointers sliding window
        minimum length -> sliding window works by shrinking

        :type s: int
        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)

        S = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            S[i] = S[i-1]+nums[i-1]

        lo, hi = 0, 1
        mini = sys.maxint
        while hi <= n:
            if S[hi]-S[lo] >= s:
                mini = min(mini, hi-lo)
                lo += 1
            else:
                hi += 1

        return mini if mini != sys.maxint else 0


if __name__ == "__main__":
    assert Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2

