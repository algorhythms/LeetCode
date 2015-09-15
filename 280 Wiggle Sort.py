"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def wiggleSort(self, nums):
        """
        Solve by enumerating examples
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for elt in sorted(nums):
            if i >= len(nums):
                i = 1
            nums[i] = elt
            i += 2