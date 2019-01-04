#!/usr/bin/python3
"""
You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""
class Solution:
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def islandPerimeter(self, grid):
        """
        There is constraint that one concrete island

        check surrounding: O(4) * O(n) = O(n)
        count side for land
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        if not grid:
            return ret
        R = len(grid)
        C = len(grid[0])
        for r0 in range(R):
            for c0 in range(C):
                if grid[r0][c0] == 1:
                    for dr, dc in self.dirs:
                        r = r0 + dr
                        c = c0 + dc
                        if r < 0 or r >= R or c < 0 or c >= C:
                            ret += 1
                        elif grid[r][c] == 0:
                            ret += 1

        return ret


if __name__ == "__main__":
    grid = [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
    ]
    assert Solution().islandPerimeter(grid) == 16
