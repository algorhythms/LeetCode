"""
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value
appears at least twice in the array, and it should return false if every element is distinct.
"""
__author__ = 'Daniel'
from collections import Counter


class Solution:
    def containsDuplicate(self, nums):
        """
        Trival
        :type nums: list[int]
        :rtype : bool
        """
        d = Counter(nums)
        for k, v in d.items():
            if v > 1:
                return True

        return False
