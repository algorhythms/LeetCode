"""
Premium Question
"""
import sys

__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def shortestDistance(self, grid):
        """
        BFS & collect all distance

        ideas:
        Pruning: don't use a fresh "visited" for each BFS. Instead, I walk only
        onto the cells that were reachable from all previous buildings. From the
        first building I only walk onto cells where grid is 0, and make them -1.
        From the second building I only walk onto cells where grid is -1, and I
        make them -2.
        -1
        -2
        -3
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        acc = [[0 for _ in xrange(n)] for _ in xrange(m)]
        reachable = [[True for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] > 0:
                    reachable[i][j] = False
                    acc[i][j] = sys.maxint

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    self.bfs(grid, acc, reachable, i, j)

        mini = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if acc[i][j] < mini and reachable[i][j]:
                    mini = acc[i][j]

        return mini if mini != sys.maxint else -1

    def bfs(self, grid, acc, reachable, x, y):
        d = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]

        q = [(x, y)]
        visited[x][y] = True  # enqueue, then visited
        while q:
            l = len(q)
            for idx in xrange(l):
                i, j = q[idx]
                acc[i][j] += d

                for dir in self.dirs:
                    I = i+dir[0]
                    J = j+dir[1]
                    if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                        q.append((I, J))
                        visited[I][J] = True

            d += 1
            q = q[l:]

        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j]:
                    reachable[i][j] = False


if __name__ == "__main__":
    assert Solution().shortestDistance(
        [[1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 1],
         [1, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 0]]) == 88
    assert Solution().shortestDistance([[1, 2, 0]]) == -1
    assert Solution().shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]) == 7
