"""
Premium Question
"""
__author__ = 'Daniel'


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


import heapq


class Solution:
    def minMeetingRooms(self, intervals):
        """

        :type intervals: list[Interval]
        :rtype: int
        """
        maxa = 0

        intervals.sort(cmp=Solution.cmp)
        end_heap = []
        for itvl in intervals:
            heapq.heappush(end_heap, itvl.end)
            while end_heap and end_heap[0] <= itvl.start:
                heapq.heappop(end_heap)

            maxa = max(maxa, len(end_heap))

        return maxa


    @staticmethod
    def cmp(a, b):
        if a.start != b.start:
            return a.start-b.start

        return a.end-b.end
