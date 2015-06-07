# -*- coding: utf-8 -*-
"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋
times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
__author__ = 'Daniel'


class Solution:
    def majorityElement(self, nums):
        """
        Algorithm:
        O(n lgn) sort and take the middle one
        O(n) Moore's Voting Algorithm
        :type nums: list[int]
        :rtype int
        """
        mjr = nums[0]
        cnt = 0
        for i, v in enumerate(nums):
            if mjr == v:
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0:
                mjr = v
                cnt = 1

        return mjr

