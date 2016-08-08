"""
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the
memory at once?
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        Hash table
        Time O(m+n)
        Memory O(m+n)
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        h1, h2 = defaultdict(int), defaultdict(int)
        for a in nums1:
            h1[a] += 1
        for b in nums2:
            h2[b] += 1

        ret = []
        for k, v in h1.items():
            cnt = min(v, h2[k])
            ret.extend([k]*cnt)

        return ret


