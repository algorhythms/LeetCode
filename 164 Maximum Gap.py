"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
"""
__author__ = 'Daniel'
import sys


class Solution:
    def maximumGap(self, nums):
        """
        Brute force O(n lgn)

        Data, gap -> distribution -> histogram
        Rough sort in bins in linear time

        :type nums: list[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        g_min = min(nums)
        g_max = max(nums)

        bin_width = max(1, (g_max-g_min)/n)
        bins_min = {}
        bins_max = {}
        for v in nums:
            bin_id = (v-g_min)/bin_width
            bins_min[bin_id] = min(bins_min.get(bin_id, sys.maxint), v)
            bins_max[bin_id] = max(bins_max.get(bin_id, -sys.maxint-1), v)

        max_gap = 0
        pre_max = g_min
        for i in xrange(0, (g_max-g_min)/bin_width+1):
            if i in bins_min:
                max_gap = max(max_gap, bins_min[i]-pre_max)
                pre_max = bins_max[i]

        return max_gap

if __name__ == "__main__":
    assert Solution().maximumGap([1, 1000]) == 999