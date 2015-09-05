# -*- coding: utf-8 -*-
"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very
right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
"""
__author__ = 'Daniel'


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Algorithms
        1. brute force
        2. heap with lazy deletion
        3. queue

        In the double-ended queue algorithm, you need to assign the queue with a meaning, in a way that you can
        access the window's max in O(1).

        Invariant: the queue is storing non-decreasing-ordered elements of current window.

        The queue stores the index rather than element
        :type nums: list[]
        :type k: int
        :rtype: list[]
        """
        q = []  # store the index
        ret = []
        n = len(nums)
        for i in xrange(n):
            while q and q[0] <= i-k:
                q.pop(0)
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                ret.append(nums[q[0]])

        return ret
