"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in
the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 <= k <= n2.
"""
import heapq


__author__ = 'Daniel'


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        Heap of list
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])

        class Node(object):
            def __init__(self, i, j):
                self.i = i
                self.j = j

            def __cmp__(self, other):
                return matrix[self.i][self.j] - matrix[other.i][other.j]

            def hasnext(self):
                return self.j+1 < n

            def next(self):
                if self.hasnext():
                    return Node(self.i, self.j + 1)

                raise StopIteration

        h = []
        for i in xrange(m):
            heapq.heappush(h, Node(i, 0))

        ret = None
        for _ in xrange(k):
            ret = heapq.heappop(h)
            if ret.hasnext():
                heapq.heappush(h, ret.next())

        return matrix[ret.i][ret.j]

    def kthSmallestError(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        i = k % n
        j = k - (i * m)
        return matrix[i][j]

if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    print Solution().kthSmallest(matrix, k)
