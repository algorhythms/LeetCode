#!/usr/bin/python3
"""
There are a number of spherical balloons spread in two-dimensional space. For
each balloon, provided input is the start and end coordinates of the horizontal
diameter. Since it's horizontal, y-coordinates don't matter and hence the
x-coordinates of start and end of the diameter suffice. Start is always smaller
than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the
x-axis. A balloon with xstart and xend bursts by an arrow shot at x if
x_start ≤ x ≤ x_end. There is no limit to the number of arrows that can be shot.
An arrow once shot keeps travelling up infinitely. The problem is to find the
minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8]
and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
import heapq


class Balloon:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __lt__(self, other):
        # __cmp__ removed in py3
        return self.e < other.e


class Solution:
    def findMinArrowShots(self, points):
        """
        greedy shot since if two balloon no overlap, then must shot separately

        heap: min, insert by s, pop by e
        Like the maximum overlapping interval

        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        points.sort(key=lambda x: x[0])
        heap = []
        for point in points:
            s, e = point
            if heap and heap[0].e < s:
                ret += 1
                heap = []

            heapq.heappush(heap, Balloon(s, e))

        if heap:
            ret += 1

        return ret


if __name__ == "__main__":
    assert Solution().findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]) == 2
