# -*- coding: utf-8 -*-
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the
kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""
__author__ = 'Daniel'
import heapq


class Solution:
    def findKthLargest(self, nums, k):
        """
        Algorithm:
        * Partial quick sort average O(n), worst case O(n^2)
        * Heap O(n lg k), kth largest element is the smallest one in the k-size heap.

        :rtype: int
        """
        h = []
        n = len(nums)
        for i, v in enumerate(nums):
            if i < k:
                heapq.heappush(h, v)
            else:
                if v <= h[0]:
                    continue
                heapq.heappop(h)
                heapq.heappush(h, v)

        return heapq.heappop(h)


if __name__ == "__main__":
    print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)

