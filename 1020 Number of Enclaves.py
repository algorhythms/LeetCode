#!/usr/bin/python3
"""
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land
square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the
boundary of the grid in any number of moves.

Example 1:
Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation:
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed
because its on the boundary.

Example 2:
Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation:
All 1s are either on the boundary or can reach the boundary.

Note:
1 <= A.length <= 500
1 <= A[i].length <= 500
0 <= A[i][j] <= 1
All rows have the same size.
"""
from typing import List


dirs = ((0, -1), (0, 1), (1, 0), (-1, 0))


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        """
        not dfs from any cell, but dfs from the edges
        """
        m, n = len(A), len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and A[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    self.dfs(A, i, j, visited)

        ret = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and not visited[i][j]:
                    ret += 1
        return ret

    def dfs(self, A, i, j, visited):
        m, n = len(A), len(A[0])
        visited[i][j] = True
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and A[I][J] == 1:
                self.dfs(A, I, J, visited)


class SolutionError:
    def __init__(self):
        self.ret = 0

    def numEnclaves(self, A: List[List[int]]) -> int:
        """
        dfs coloring
        """
        m, n = len(A), len(A[0])
        visited = [[None for _ in range(n)] for _ in range(m)]  # 0 not off, 1 off
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and A[i][j] == 1:
                    self.dfs(A, i, j, visited)
        return self.ret

    def dfs(self, A, i, j, visited):
        m, n = len(A), len(A[0])
        visited[i][j] = 0
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if not (0 <= I < m and 0 <= J < n):
                visited[i][j] = 1
                return True
            if visited[I][J] == 1:
                visited[i][j] = 1
                return True
            if visited[I][J] is None and A[I][J] == 1 and self.dfs(A, I, J, visited):
                visited[i][j] = 1
                return True

        self.ret += 1
        return False
