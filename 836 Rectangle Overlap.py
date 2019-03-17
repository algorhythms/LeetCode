#!/usr/bin/python3
"""
A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its
top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be
clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Notes:

Both rectangles rec1 and rec2 are lists of 4 integers.
All coordinates in rectangles will be between -10^9 and 10^9.
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        """
        De Morgan's Law
           0      1       2        3
        [left_x, left_y, right_x, right_y]

        Non-overlap if on the left, right, top, bottom
        """
        return not (
            rec1[2] <= rec2[0] or  # left
            rec1[0] >= rec2[2] or  # right
            rec1[1] >= rec2[3] or  # top
            rec1[3] <= rec2[1]     # bottom
        )


    def isRectangleOverlap_error(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] > rec2[0]:
            return self.isRectangleOverlap(rec2, rec1)

        return (
            rect1[0] < rect2[0] < rec1[2] and
            (
                rec2[1] < rect1[3] < rect2[3] or
                rec2[3] < rect1[3] < rect2[1]
            )
        )
