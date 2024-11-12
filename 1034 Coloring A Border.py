#!/usr/bin/python3
"""
You are given an m x n integer matrix grid, and three integers row, col, and color. Each value in the grid represents the color of the grid square at that location.

Two squares are called adjacent if they are next to each other in any of the 4 directions.

Two squares belong to the same connected component if they have the same color and they are adjacent.

The border of a connected component is all the squares in the connected component that are either adjacent to (at least) a square not in the component, or on the boundary of the grid (the first or last row or column).

You should color the border of the connected component that contains the square grid[row][col] with color.

Return the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
Output: [[3,3],[3,2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
Output: [[1,3,3],[2,3,3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
Output: [[2,2,2],[2,1,2],[2,2,2]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j], color <= 1000
0 <= row < m
0 <= col < n
"""


class Solution:
    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        """
        In any direction, it has other color then color it
        in four direction, same color, then not color
        """
        origin = grid[row][col]
        m = len(grid)
        n = len(grid[0])
        visited = [
            [False for j in range(n)]
            for i in range(m)
        ]
        should_color = [
            [False for j in range(n)]
            for i in range(m)
        ]
        self.dfs(grid, row, col, visited, should_color)

        for i in range(m):
            for j in range(n):
                if should_color[i][j]:
                    grid[i][j] = color

        return grid

    def dfs(self, grid, i, j, visited, should_color):
        m = len(grid)
        n = len(grid[0])

        visited[i][j] = True
        cnt = 0
        for d in self.dirs:
            I = i + d[0]
            J = j + d[1]
            if 0 <= I < m and 0 <= J < n:
                if not visited[I][J] and grid[I][J] == grid[i][j]:
                    self.dfs(grid, I, J, visited, should_color)

                if grid[I][J] == grid[i][j]:
                    cnt += 1
        if cnt < 4:
            should_color[i][j] = True 
