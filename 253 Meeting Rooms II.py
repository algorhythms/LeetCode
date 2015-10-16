"""
Premium Question
Find the maximum number of overlapped intervals
"""
import heapq
import operator


__author__ = 'Daniel'


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        """

        :type intervals: list[Interval]
        :rtype: int
        """
        maxa = 0

        intervals.sort(key=operator.attrgetter("start"))
        h_end = []
        for itvl in intervals:
            heapq.heappush(h_end, itvl.end)
            while h_end and h_end[0] <= itvl.start:
                heapq.heappop(h_end)

            maxa = max(maxa, len(h_end))

        return maxa