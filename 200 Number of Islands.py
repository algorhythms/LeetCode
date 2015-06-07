"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and
is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""
__author__ = 'Daniel'


class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid):
        """
        :type grid: list[list[str]]
        :rtype: int
        """
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        cnt = 0
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and grid[i][j] == "1":
                    self.dfs(grid, i, j, visited)
                    cnt += 1

        return cnt

    def dfs(self, grid, i, j, visited):
        """
        dfs to mark visited
        """
        m = len(grid)
        n = len(grid[0])
        visited[i][j] = True

        for dir in self.dirs:
            n_i = i+dir[0]
            n_j = j+dir[1]
            if 0 <= n_i < m and 0 <= n_j < n and not visited[n_i][n_j] and grid[n_i][n_j] == "1":
                self.dfs(grid, n_i, n_j, visited)


if __name__ == "__main__":
    assert Solution().numIslands(["1", "1"]) == 1