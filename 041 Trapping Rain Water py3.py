#!/usr/bin/python3
"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
this case, 6 units of rain water (blue section) are being trapped.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        At each position, the water is determined by the left and right max

        Let lefts[i] be the max(height[:i])
        Let rights[i] be the max(height[i:])
        """
        n = len(height)
        lefts = [0 for _ in range(n+1)]
        rights = [0 for _ in range(n+1)]
        for i in range(1, n+1):  # i, index of lefts
            lefts[i] = max(lefts[i-1], height[i-1])
        for i in range(n-1, -1, -1):
            rights[i] = max(rights[i+1], height[i])

        ret = 0
        for i in range(n):
            ret += max(
                0,
                min(lefts[i], rights[i+1]) - height[i]
            )
        return ret
