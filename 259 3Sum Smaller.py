"""
Premium Question
"""
__author__ = 'Daniel'


class Solution:
    def threeSumSmaller(self, nums, target):
        """

        :type nums: list[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        cnt = 0
        n = len(nums)
        for i in xrange(n-2):
            j = i+1
            k = n-1
            while j < k:
                if nums[i]+nums[j]+nums[k] < target:
                    cnt += k-j
                    j += 1
                else:
                    k -= 1

        return cnt