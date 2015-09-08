"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

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
        Algorithm:
        Hashmap, but to save space, use the array itself as the hashmap

        Notice:
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
        Above is wrong, since evaluate from left to right; thus, when nums[nums[i]] on RHS is None, on LHS, nums[i] is
        eval to None and nums[nums[i]] indexes by None, causing errors.

        Alternatively, it is correct that:
            nums[nums[i]], nums[i]= nums[i], nums[nums[i]]

        To be safe, just use:
            j = nums[i]
            nums[i], nums[j] = nums[j], nums[i]

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

            else:
                i += 1

        if not num_n:
            return n

        return nums.index(None)


if __name__ == "__main__":
    assert Solution().missingNumber([2, 0]) == 1
