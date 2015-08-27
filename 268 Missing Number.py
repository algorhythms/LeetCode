"""
iven an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space
complexity?
"""
__author__ = 'Daniel'


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_n = None
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] == n:
               num_n = nums[i]
               nums[i] = None
               i += 1

            elif nums[i] is not None and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

            else:
                i += 1

        if not num_n:
            return n

        return nums.index(None)

if __name__ == "__main__":
    assert Solution().missingNumber([2, 0]) == 1
