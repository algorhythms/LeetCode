#!/usr/bin/python3
"""
Given a non-empty array containing only positive integers, find if the array can
be partitioned into two subsets such that the sum of elements in both subsets is
equal.
"""
from collections import defaultdict


class Solution:
    def canPartition(self, nums):
        """
        0/1 Knapsack problem

        Carefully define the state:
        Let d[i][s] be # subset of nums[:i+1], can be sum to s

        Transition function:
        d[i][s] = d[i-1][s] + d[i-1][s-nums[i]]
                = case not choose nums[i] + case choose nums[i]

        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        d = defaultdict(lambda: defaultdict(int))
        d[0][0] = 1
        d[0][nums[0]] = 1

        for i in range(1, len(nums)):
            for v in range(target + 1):
                d[i][v] = d[i-1][v] + d[i-1][v-nums[i]]

        return any(d[i][target] > 0 for i in range(len(nums)))

    def canPartition_TLE(self, nums):
        """
        subset rather than sub array
        positive number only

        dfs with pruning O(2^n), whether to choose the number or not

        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        return self.dfs(nums, 0, target)

    def dfs(self, nums, idx, target):
        """Find a subset that sum to target"""
        if not idx < len(nums):
            return False
        if nums[idx] == target:
            return True
        if nums[idx] > target:
            return False

        return (
            self.dfs(nums, idx + 1, target) or   # not take nums[idx]
            self.dfs(nums, idx + 1, target - nums[idx])  # take nums[idx]
        )


if __name__ == "__main__":
     assert Solution().canPartition([1, 5, 11, 5]) == True
     assert Solution().canPartition([1, 2, 3, 5]) == False
