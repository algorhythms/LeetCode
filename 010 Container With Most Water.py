"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.

Note: You may not slant the container.
"""
__author__ = 'Danyang'


class Solution:
    def maxArea(self, height):
        """
        Two pointers scanning
        starting from two ends since x-coordinate is maximized

        Different from 041 Trapping Rain Water, since here it only considers two lines
        :param height: array
        :return: max area, integer
        """
        start = 0
        end = len(height)-1

        max_area = -1 << 32
        while start < end:
            area = min(height[start], height[end])*(end-start)
            max_area = max(area, max_area)

            # move the shorter boarder
            # move two pointers
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

