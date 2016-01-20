# -*- coding: utf-8 -*-
"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a
distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the
x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that
0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on
an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10],
[19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that
uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point,
where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height.
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24,
0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5],
[7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output
as such: [...[2 3], [4 5], [12 7], ...]
"""
__author__ = 'Daniel'
from collections import defaultdict, namedtuple
import heapq


class Building(object):
    def __init__(self, h):
        self.h = h
        self.deleted = False  # lazy deletion

    def __cmp__(self, other):
        # Reverse order by height to get max-heap
        assert isinstance(other, Building)
        return other.h - self.h

# An event represents the buildings that start and end at a particular
# x-coordinate.
Event = namedtuple('Event', 'starts ends')


class Solution:
    def getSkyline(self, buildings):
        """
        Sweep line
        The change of skyline only happens at start and end of buildings.

        Treat a building as entering line and leaving line
        :type buildings: list[list[int]]
        :rtype: list[list[int]]
        """
        # Map from x-coordinate to event.
        events = defaultdict(lambda: Event(starts=[], ends=[]))
        for left, right, height in buildings:
            building = Building(height)
            events[left].starts.append(building)  # possible multiple building at the same x-coordinate.
            events[right].ends.append(building)

        heap_h = []  # Heap of buildings currently standing.
        cur_h = 0  # current max height of standing buildings. the current skyline
        ret = []
        # Process events in order by x-coordinate.
        for x, event in sorted(events.items()):  # sort the dictionary by key
            for building in event.starts:
                heapq.heappush(heap_h, building)
            for building in event.ends:
                building.deleted = True

            # Pop any finished buildings from the top of the heap.
            # To avoid using multiset - lazy deletion.
            while heap_h and heap_h[0].deleted:
                heapq.heappop(heap_h)

            # Top of heap (if any) is the highest standing building, so
            # its height is the current height of the skyline.
            new_h = heap_h[0].h if heap_h else 0

            if new_h != cur_h:
                cur_h = new_h
                ret.append([x, cur_h])

        return ret


if __name__ == "__main__":
    assert Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]) == \
           [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]