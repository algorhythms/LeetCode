#!/usr/bin/python3
"""
Given a set of intervals, for each of the interval i, check if there exists an
interval j whose start point is bigger than or equal to the end point of the
interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which
means that the interval j has the minimum start point to build the "right"
relationship for interval i. If the interval j doesn't exist, store -1 for the
interval i. Finally, you need output the stored value of each interval as an
array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
"""
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def new(cls, lst):
        return [
            cls(s, e)
            for s, e in lst
        ]

from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals):
        """
        given e, find the right s - bisect

        :type intervals: List[Interval]
        :rtype: List[int]
        """
        indexes = {
            itv.start: idx
            for idx, itv in enumerate(intervals)
        }
        starts = list(sorted(indexes.keys()))
        ret = []
        for itv in intervals:
            idx = bisect_left(starts, itv.end)
            if idx >= len(starts):
                ret.append(-1)
            else:
                ret.append(
                    indexes[starts[idx]]
                )

        return ret


if __name__ == "__main__":
    assert Solution().findRightInterval(Interval.new([ [3,4], [2,3], [1,2] ])) == [-1, 0, 1]
    assert Solution().findRightInterval(Interval.new([ [1,2] ])) == [-1]
    assert Solution().findRightInterval(Interval.new([ [1,4], [2,3], [3,4] ])) == [-1, 2, -1]
