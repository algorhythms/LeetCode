"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
__author__ = 'Danyang'
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge_error(self, intervals):
        """
        scanning. No algorithm
        math
        :param intervals: a list of Interval
        :return: a list of Interval
        """
        if not intervals:
            return []
        result = []
        result.append(intervals[0])
        for interval in intervals[1:]:
            if result[-1].end<interval.start:
                result.append(interval)
                continue
            if result[-1].start<=interval.start<=result[-1].end and result[-1].end<=interval.end:
                result[-1].end = interval.end
                continue
            if interval.start<=result[-1].start and result[-1].end<=interval.end:
                result[-1] = interval
                continue
            if result[-1].start<=interval.start<result[-1].end and result[-1].start<=interval.end<result[-1].end:
                result.append(interval)
                continue
            if interval.start<result[-1].start and result[-1].start<=interval.end<result[-1].end:
                result[-1].start = interval.start
                continue
            if interval.end<result[-1].start:
                result.append(result)
                continue


        return result


    def merge(self, intervals):
        """
        scanning. No algorithm
        math
        :param intervals: a list of Interval
        :return: a list of Interval
        """
        if not intervals:
            return []

        intervals.sort(cmp=lambda a, b: a.start-b.start)
        result = [intervals[0]]
        for cur in intervals[1:]:
            pre = result[-1]
            if cur.start<=pre.end:  # overlap
                pre.end = max(pre.end, cur.end)
            else:
                result.append(cur)

        return result



