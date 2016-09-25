"""
Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies
you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall
is too strong to be destroyed.
Note that you can only put the bomb at an empty cell.

Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""
__author__ = 'Daniel'


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        Brute force: O(n * n^2)
        Place the bomb around boundary
        The result of boundary bomb can be reused - dp

        The time complexity is O(m + n)
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        rows = [0 for _ in xrange(m)]
        cols = [0 for _ in xrange(n)]
        gmax = 0
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or grid[i-1][j] == 'W':
                    cols[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] == 'E':
                            cols[j] += 1
                        elif grid[k][j] == 'W':
                            break

                if j == 0 or grid[i][j-1] == 'W':
                    rows[i] = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'E':
                            rows[i] += 1
                        elif grid[i][k] == 'W':
                            break

                if grid[i][j] == '0':
                    gmax = max(gmax, rows[i] + cols[j])

        return gmax

if __name__ == "__main__":
    assert Solution().maxKilledEnemies(["0E00", "E0WE", "0E00"]) == 3