"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
"""
import sys

__author__ = 'Daniel'


class Solution(object):
    def increasingTriplet(self, nums):
        """
        Brute force: O(N^3)

        dp: O(N)
        :type nums: List[int]
        :rtype: bool
        """
        min1 = sys.maxint
        min2 = sys.maxint
        for e in nums:
            if e < min1:
                min1 = e
            elif e != min1 and e < min2:
                min2 = e
            elif e > min2:
                return True

        return False

    def increasingTripletError(self, nums):
        """
        use stack
        :type nums: List[int]
        :rtype: bool
        """
        stk = []
        for elt in nums:
            while stk and stk[-1] >= elt:
                stk.pop()

            stk.append(elt)
            if len(stk) >= 3:
                return True

        return False
