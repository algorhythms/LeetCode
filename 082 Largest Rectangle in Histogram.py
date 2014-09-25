"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of
largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""
__author__ = 'Danyang'
class Solution:
    def largestRectangleArea_TLE(self, height):
        """
        O(n*n)
        :param height: a list of int
        :return: int
        """
        if not height:
            return 0

        max_area = -1<<32
        for ind, val in enumerate(height):
            min_h = val
            max_area = max(max_area, val*1)
            for j in xrange(ind, -1, -1):
                min_h = min(min_h, height[j])
                current_area = min_h*(ind-j+1)
                max_area = max(max_area, current_area)

        return max_area


    def largestRectangleArea(self, height):
        """
        O(n*n) + prune

        O(n) #TODO

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        if not height:
            return 0

        max_area = -1<<32
        for ind, val in enumerate(height):
            if ind+1<len(height) and val<=height[ind+1]:  # find until peak
                continue
            min_h = val
            max_area = max(max_area, val*1)
            for j in xrange(ind, -1, -1):
                min_h = min(min_h, height[j])
                current_area = min_h*(ind-j+1)
                max_area = max(max_area, current_area)

        return max_area




