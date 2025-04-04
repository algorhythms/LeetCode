"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
import sys 


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS
        """
        if grid[0][0] != 0:
            return -1
        
        M = len(grid)
        N = len(grid[0])
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        q = [(0, 0)]
        dist = [
            [sys.maxsize for _ in range(N)]
            for _ in range(M)
        ]
        dist[0][0] = 1
        while q:
            new_q = []
            for i, j in q:
                d = dist[i][j]
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < M and 0 <= J < N and grid[I][J] == 0:
                        if dist[I][J] > d + 1:
                            dist[I][J] = d + 1
                            new_q.append((I, J))
            q = new_q
        
        ret = dist[M-1][N-1]
        if ret != sys.maxsize:
            return ret
        return -1