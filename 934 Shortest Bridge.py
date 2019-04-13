#!/usr/bin/python3
"""
In a given 2D binary array A, there are two islands.  (An island is a
4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1
island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that
the answer is at least 1.)

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Note:
1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
from typing import List


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """
        market component 1 and component 2
        iterate 0 and BFS, min(dist1 + dist2 - 1)?
        O(N * N) high complexity

        BFS grow from 1 component
        """
        m, n = len(A), len(A[0])
        # coloring
        colors = [[None for _ in range(n)] for _ in range(m)]
        color = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and colors[i][j] is None:
                    self.dfs(A, i, j, colors, color)
                    color += 1
        assert color == 2

        # BFS
        step = 0
        q = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if colors[i][j] == 0:
                    visited[i][j] = True
                    q.append((i, j))

        while q:
            cur_q = []
            for i, j in q:
                for I, J in self.nbr(A, i, j):
                    if not visited[I][J]:
                        if colors[I][J] == None:
                            visited[I][J] = True   # pre-check, dedup
                            cur_q.append((I, J))
                        elif colors[I][J] == 1:
                            return step
            step += 1
            q = cur_q

        raise

    def nbr(self, A, i, j):
        m, n = len(A), len(A[0])
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n:
                yield I, J

    def dfs(self, A, i, j, colors, color):
        colors[i][j] = color
        for I, J in self.nbr(A, i, j):
            if colors[I][J] is None and A[I][J] == 1:
                self.dfs(A, I, J, colors, color)


if __name__ == "__main__":
    assert Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]) == 1
