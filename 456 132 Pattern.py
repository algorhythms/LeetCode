#!/usr/bin/python3
"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence
ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes
a list of n numbers as input and checks whether there is a 132 pattern in the
list.

Note: n will be less than 15,000.
"""


class Solution:
    def find132pattern(self, nums):
        """
        Brute force i, j, k O(n^3)

        Optimize: I only need to keep the max number for the middle. O(N^2)

        Need better optimization?
        I need to keep both the min and max number for A[:i] when scanning A[i]
        min must be at left of max

        When scanning A[i], we need a list to keep both the min and max interval
        [min, max]. The list maintains intervals that end at A[i-1] and start at
        the min(A[:i-1])
        0. The max is not increasing, thus can only keep A[i-1]
        1. F(i) = min(A[:i-1]) is strictly non-increasing (softly decreasing)
        2. We don't need to keep any internal that interval.end <= A[i]
        3. The list can be replaced with stack

        O(N) since every number enters and pops the stack once

        :type nums: List[int]
        :rtype: bool
        """
        stack = []  # List[Interval]
        mini = float('Inf')
        for v in nums:
            while stack and stack[-1][1] <= v:  # error when < (e.g. [-2, 1, 1])
                stack.pop()
            if stack and stack[-1][0] < v:
                return True
            mini = min(mini, v)
            stack.append((mini, v))

        return False


    def find132pattern_TLE(self, nums):
        """
        Brute force i, j, k O(n^3)

        Optimize: you only need to keep the max number for the middle. O(N^2)
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            maxa = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if nums[j] < maxa:
                        return True
                    maxa = max(maxa, nums[j])

        return False


if __name__ == "__main__":
    assert Solution().find132pattern([1, 2, 3, 4]) == False
    assert Solution().find132pattern([3, 1, 4, 2]) == True
    assert Solution().find132pattern([-1, 3, 2, 0]) == True
    assert Solution().find132pattern([-2, 1, 1]) == True
