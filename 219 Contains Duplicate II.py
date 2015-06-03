"""
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the difference between i and j is at most k.
"""
__author__ = 'Daniel'
import heapq
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        hash with heap

        :rtype: bool
        """
        d = defaultdict(list)
        for i, v in enumerate(nums):
            heapq.heappush(d[v], i)

        for v in d.values():
            if len(v) > 1:
                pre = heapq.heappop(v)
                while v:
                    cur = heapq.heappop(v)
                    if cur-pre <= k:
                        return True
                    pre = cur

        return False