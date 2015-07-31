"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of
largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""
import sys
__author__ = 'Danyang'


class Solution:
    def largestRectangleArea(self, height):
        """
        O(2*n)
        every bar at most enter the stack once and is popped out once.

        Algorithm: Stack.
        Keep a stack storing the bars increasing order, then calculate the area by popping out the stack to get the
        currently lowest bar which determines the height of the rectangle.

        The popping out is triggered when height being scanned violates increasing order. Keep popping out until not
        violate the increasing order.

        When calculate the area: area = height[last]*( i-(inc_stack[-1]+1) ) rather than area = height[last] * (i-last),
        since originally from inc_stack[-1]+1 to last are higher bars already popped out, which should be included in
        the calculation.

        pay attention to corner case

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        if not height:
            return 0

        n = len(height)
        gmax = -sys.maxint-1
        inc_stack = []  # store the idx, increasing stack

        for i in xrange(n):
            while inc_stack and height[inc_stack[-1]] > height[i]:
                last = inc_stack.pop()
                if inc_stack:  # calculate area when popping
                    area = height[last]*(i-(inc_stack[-1]+1))
                else:
                    area = height[last]*i
                gmax = max(gmax, area)

            inc_stack.append(i)

        # after processing all heights, process the remaining stack
        i = n
        while inc_stack:
            last = inc_stack.pop()
            if inc_stack:
                area = height[last]*(i-(inc_stack[-1]+1))
            else:
                area = height[last]*i
            gmax = max(gmax, area)

        return gmax

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


    def largestRectangleArea_complex(self, height):
        """
        O(n*n) + prune

        starting from every column, scan backward to calculate the max possible area under current column

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        if not height:
            return 0

        global_max = -1<<32
        for ind, val in enumerate(height):
            if ind+1<len(height) and val<=height[ind+1]:  # PRUNE, find until peak
                continue

            min_h = val
            global_max = max(global_max, min_h*1)
            for j in xrange(ind, -1, -1):  # scanning backward
                min_h = min(min_h, height[j])
                current_area = min_h*(ind-j+1)
                global_max = max(global_max, current_area)

        return global_max


    def largestRectangleArea_error(self, height):
        """
        O(n)

        Algorithm: Stack.

        reference: http://fisherlei.blogspot.sg/2012/12/leetcode-largest-rectangle-in-histogram.html
        :param height: a list of int
        :return: int
        """
        if not height:
            return 0

        length = len(height)
        global_max = -1<<32
        inc_stack = []  # store the pointer

        i = 0
        while i<length:
            if not inc_stack or height[i]>=height[inc_stack[-1]]:
                inc_stack.append(i)
                i += 1
            else:
                last = inc_stack.pop()
                if inc_stack:
                    area = height[last] * (i-last)
                else:
                    area = height[last] * i
                global_max = max(global_max, area)

        # remaining stack
        while inc_stack:
            last = inc_stack.pop()
            if inc_stack:
                area = height[last]*(i-last)
            else:
                area = height[last]*i
            global_max = max(global_max, area)
        return global_max


if __name__=="__main__":
    # height = [2, 1, 2]
    height = [4, 2, 0, 3, 2, 5]
    assert Solution().largestRectangleArea(height) == Solution().largestRectangleArea_complex(height)




