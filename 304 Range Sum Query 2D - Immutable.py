# -*- coding: utf-8 -*-
"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1,
col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains
sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""
__author__ = 'Daniel'


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        dp F[i][j] = F[i-1][j]+F[i][j-1]-F[i-1][j-1]+mat[i][j]
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0:
            self.F = None
            return

        n = len(matrix[0])
        self.F = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.F[i][j] = self.F[i-1][j]+self.F[i][j-1]-self.F[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        """
        if not self.F:
            return 0

        return self.F[row2+1][col2+1] - self.F[row2+1][col1] - self.F[row1][col2+1] + self.F[row1][col1]