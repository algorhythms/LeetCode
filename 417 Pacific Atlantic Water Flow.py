#!/usr/bin/python3
"""
Given an m x n matrix of non-negative integers representing the height of each
nit cell in a continent, the "Pacific ocean" touches the left and top edges of
the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to
another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and
Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
parentheses in above matrix).
"""
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution:
    def pacificAtlantic(self, matrix):
        """
        dfs, visisted O(1)
        Similar to Trapping Rainwater II (BFS + heap), but no need to record
        volume, thus, dfs is enough.

        Similar to longest increasing path

        Starting from the edge point rather than any point, dfs visit the
        possible cell

        Complexity analysis, although a cell can be checked multiple times
        (at most 4 times); but only perform 1 dfs on each cell; thus
        O(mn)

        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])  # row, col
        # don't do [[False] * n ] * m, memory management, all rows reference the same row
        P = [[False for _ in range(n)] for _ in range(m)]
        A = [[False for _ in range(n)] for _ in range(m)]

        # starting from edge point
        for i in range(m):
            self.dfs(matrix, i, 0, P)
            self.dfs(matrix, i, n-1, A)

        for j in range(n):
            self.dfs(matrix, 0, j, P)
            self.dfs(matrix, m-1, j, A)

        ret = [
            [i, j]
            for i in range(m)
            for j in range(n)
            if P[i][j] and A[i][j]
        ]
        return ret

    def dfs(self, matrix, i, j, C):
        # check before dfs (to be consistent)
        C[i][j] = True
        m, n = len(matrix), len(matrix[0])
        for x, y in dirs:
            I = i + x
            J = j + y
            if 0 <= I < m and 0 <= J < n and matrix[i][j] <= matrix[I][J]:
                if not C[I][J]:
                    self.dfs(matrix, I, J, C)


    def pacificAtlantic_error(self, matrix):
        """
        DP
        dfs, visisted O(1)
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])  # row, col
        P = [[False] * n ] * m
        A = [[False] * n ] * m

        visisted = [[False] * n ] * m
        for i in range(m):
            for j in range(n):
                self.dfs_error(matrix, i, j, visisted, P, lambda i, j: i < 0 or j <0)

        visisted = [[False] * n ] * m
        for i in range(m):
            for j in range(n):
                self.dfs_error(matrix, i, j, visisted, A, lambda i, j: i >= m or j >= n)

        ret = [
            [i, j]
            for i in range(m)
            for j in range(n)
            if P[i][j] and A[i][j]
        ]
        return ret


    def dfs_error(self, matrix, i, j, visisted, C, predicate):
        m, n = len(matrix), len(matrix[0])
        if visisted[i][j]:
            return C[i][j]

        visisted[i][j] = True
        for x, y in dirs:
            i2 = i + x
            j2= j + y
            if 0 <= i2 < m and 0 <= j2 < n:
                if self.dfs_error(matrix, i2, j2, visisted, C, predicate) and matrix[i][j] >= matrix[i2][j2]:
                    C[i][j] = True
            elif predicate(i2, j2):
                C[i][j] = True

        return C[i][j]


if __name__ == "__main__":
    assert Solution().pacificAtlantic([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
