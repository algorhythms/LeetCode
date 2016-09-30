"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-
zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

__author__ = 'Daniel'


class Solution(object):
    def moveZeroes(self, nums):
        """
        Two pointers at the left side
        Pivot
        """
        left = -1
        for i in xrange(len(nums)):
            if nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]


class SolutionCount(object):
    def moveZeroes(self, nums):
        """
        In-place
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for elt in nums:
            if elt != 0:
                nums[cnt] = elt
                cnt += 1

        for j in xrange(cnt, len(nums)):
            nums[j] = 0


if __name__ == "__main__":
    lst = [0, 1, 0, 3, 12]
    Solution().moveZeroes(lst)
    assert lst == [1, 3, 12, 0, 0]
