"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.

Note: This question is the same as 1765: https://leetcode.com/problems/map-of-highest-peak/
"""
import sys
from collections import deque


class SolutionError:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        * dfs every cell
        * with memoization 

        dfs + visited 

        dfs is wrong
        """
        self.mat = mat
        self.M = len(mat)
        self.N = len(mat[0])
        self.dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        visited = [
            [False for _ in range(self.N)]
            for _ in range(self.M)
        ]
        ret = [
            [sys.maxsize for _ in range(self.N)]
            for _ in range(self.M)
        ]
        for i in range(self.M):
            for j in range(self.N):
                self.nearest(i, j, visited, ret)
            
        return ret

    def nearest(self, i, j, visited, ret):
        if visited[i][j]:
            return ret[i][j]

        visited[i][j] = True
        if self.mat[i][j] == 0:
            ret[i][j] = 0
            return 0

        for di, dj in self.dirs:
            I = i + di
            J = j + dj
            if 0 <= I < self.M and 0 <= J < self.N:
                nbr = self.nearest(I, J, visited, ret)
                ret[i][j] = min(ret[i][j], nbr + 1)
        
        return ret[i][j]


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        BFS 
        """
        q = deque()
        M = len(mat)
        N = len(mat[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ret = [
            [sys.maxsize for _ in range(N)]
            for _ in range(M)
        ]
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 0:
                    ret[i][j] = 0
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for di, dj in dirs:
                I = i + di
                J = j + dj
                # update nbr
                if 0 <= I < M and 0 <= J < N:
                    cur = ret[i][j] + 1
                    if ret[I][J] > cur: 
                        ret[I][J] = cur
                        q.append((I, J))  # add to pending queue
        
        return ret 
