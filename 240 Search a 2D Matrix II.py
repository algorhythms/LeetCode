"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
__author__ = 'Daniel'


class Solution:
    def searchMatrix(self, matrix, target):
        """

        :type matrix: list[int][int]
        :type target: int
        :rtype: bool
        """
        try:
            m = len(matrix)
            n = len(matrix[0])

            lst = [matrix[i][0] for i in xrange(m)]
            row_by_first = self.bisect(lst, target)
            lst = [matrix[i][-1] for i in xrange(m)]
            row_by_last = self.bisect(lst, target, False)
            for i in range(row_by_first, row_by_last-1, -1):
                col = self.bisect(matrix[i], target)
                if matrix[i][col] == target:
                    return True

            return False
        except IndexError:
            return False

    def bisect(self, A, t, lower=True):
        lo = 0
        hi = len(A)
        while lo < hi:
            mid = (lo+hi)/2
            if A[mid] == t:
                return mid
            elif A[mid] < t:
                lo = mid+1
            else:
                hi = mid
        if lower:
            return lo-1
        else:
            return lo

if __name__ == "__main__":
    assert Solution().searchMatrix([[1, 4], [2, 5]], 4) == True