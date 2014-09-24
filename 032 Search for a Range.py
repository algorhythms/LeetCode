"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

__author__ = 'Danyang'
class Solution:
    def searchRange(self, A, target):
        """
        Binary Search Twice
        Notice the low-bound & high-bound binary search

        :param A: a list of integers
        :param target: an integer to be searched
        :return: a list of length 2, [index1, index2]
        """
        result = []
        length = len(A)

        # low-bound binary search
        start = 0
        end = length  # [0, length)
        while start<end:
            mid = (start+end)/2
            if A[mid]<target:  # NOTICE: less than
                start = mid+1
            else:
                end = mid

        if start<length and A[start]==target:
            result.append(start)
        else:
            return [-1, -1]

        # high-bound binary search
        start = start
        end = length  # no "-1" # [0, length)
        while start<end:
            mid = (start+end)/2
            if A[mid]<=target:  # NOTICE: less than or equal
                start = mid+1
            else:
                end = mid

        result.append(start-1)
        return result