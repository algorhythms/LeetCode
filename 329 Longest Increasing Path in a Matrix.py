"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move
outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.cache = None
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    def longestIncreasingPath(self, matrix):
        """
        dfs + cache
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0

        m, n = len(matrix), len(matrix[0])
        self.cache = [[None for _ in xrange(n)] for _ in xrange(m)]
        gmax = 1
        for i in xrange(m):
            for j in xrange(n):
                gmax = max(gmax, self.longest(matrix, i, j))

        return gmax

    def longest(self, matrix, i, j):
        """
        Strictly increasing, thus no need to have a visited matrix
        """
        if not self.cache[i][j]:
            m, n = len(matrix), len(matrix[0])
            maxa = 1
            for d in self.dirs:
                I, J = i + d[0], j + d[1]
                if 0 <= I < m and 0 <= J < n and matrix[I][J] > matrix[i][j]:
                    maxa = max(maxa, 1 + self.longest(matrix, I, J))

            self.cache[i][j] = maxa

        return self.cache[i][j]


if __name__ == "__main__":
    assert Solution().longestIncreasingPath([
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]) == 4
