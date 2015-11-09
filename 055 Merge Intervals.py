"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""
__author__ = 'Danyang'


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, itvls):
        """
        scanning. No algorithm
        math
        :param itvls: a list of Interval
        :return: a list of Interval
        """
        if not itvls:
            return []

        itvls.sort(key=lambda x: x.start)  # sort first, since time complexity less than brute force
        ret = [itvls[0]]
        for cur in itvls[1:]:
            pre = ret[-1]
            if cur.start <= pre.end:  # overlap
                pre.end = max(pre.end, cur.end)
            else:
                ret.append(cur)

        return ret

    def merge_error(self, itvls):
        """
        scanning. No algorithm
        math
        :param itvls: a list of Interval
        :return: a list of Interval
        """
        if not itvls:
            return []

        ret = [itvls[0]]
        for interval in itvls[1:]:
            if ret[-1].end < interval.start:
                ret.append(interval)
                continue
            if ret[-1].start <= interval.start <= ret[-1].end <= interval.end:
                ret[-1].end = interval.end
                continue
            if interval.start <= ret[-1].start and ret[-1].end <= interval.end:
                ret[-1] = interval
                continue
            if ret[-1].start <= interval.start < ret[-1].end and ret[-1].start <= interval.end < ret[-1].end:
                ret.append(interval)
                continue
            if interval.start < ret[-1].start <= interval.end < ret[-1].end:
                ret[-1].start = interval.start
                continue
            if interval.end < ret[-1].start:
                ret.append(ret)
                continue

        return ret
