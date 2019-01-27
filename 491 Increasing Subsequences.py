#!/usr/bin/python3
"""
Given an integer array, your task is to find all the different possible
increasing subsequences of the given array, and the length of an increasing
subsequence should be at least 2 .

Example:
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
[4,7,7]]
Note:
The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be
considered as a special case of increasing sequence.
"""


class Solution:
    def findSubsequences(self, nums):
        """
        2nd approach
        Maintain the current increasing subsequence and iterate them to grow it
        Same complexity as the 1st approach since both needs to iterate the
        subsequences

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subs = set()
        for n in nums:
            subs |= set([
                sub + (n,)
                for sub in subs
                if n >= sub[-1]
            ])
            subs.add((n,))
            
        return [
            list(sub)
            for sub in subs
            if len(sub) >= 2
        ]


    def findSubsequences(self, nums):
        """
        1st approach.
        F[i] records the increasing subsequence ends at A[i]
        F[i] = F[j] + A[i].
        iterating F[j] is exponential

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        F = [
            [(nums[i],)]
            for i in range(l)
        ]
        ret = set()
        for i in range(1, l):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for t in F[j]:
                        cur = t + (nums[i],)
                        ret.add(cur)
                        F[i].append(cur)

        return list(map(list, ret))
