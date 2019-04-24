#!/usr/bin/python3
"""
In a N x N grid representing a field of cherries, each cell is one of three
possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the
rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down
through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through
valid path cells;
When passing through a path cell containing a cherry, you pick it up and the
cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be
collected.

Example 1:
Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes
[[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more
cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Note:
grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""
from typing import List


class Solution:
    def __init__(self):
        self.cache = {}

    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        DP go and back
        Go back probably related - yes it is related

        Instead of walking from end to beginning, let's reverse the second leg
        of the path, so we are only considering two paths from the beginning to
        the end.
        """
        return max(0, self.F(grid, 0, 0, 0))

    def F(self, grid, r1, c1, r2):
        n = len(grid)
        if (r1, c1, r2) not in self.cache:
            ret = float("-inf")
            c2 = r1 + c1 - r2   # r1 + c1 == r2 + c2
            if 0 <= r1 < n and 0 <= c1 < n and 0 <= r2 < n and 0 <= c2 < n:
                if grid[r1][c1] != -1 and grid[r2][c2] != -1:
                    ret = 0
                    ret += grid[r1][c1]
                    if r1 != r2:
                        ret += grid[r2][c2]

                    if r1 == n - 1 and c1 == n - 1:
                        pass  # seed, otherwise -inf 
                    else:
                        ret += max(
                            self.F(grid, r1+1, c1, r2+1),   # down, down
                            self.F(grid, r1+1, c1, r2),  # down, right
                            self.F(grid, r1, c1+1, r2+1),  # right, down
                            self.F(grid, r1, c1+1, r2),  # right, right
                        )

            self.cache[r1, c1, r2] = ret

        return self.cache[r1, c1, r2]


if __name__ == "__main__":
    assert Solution().cherryPickup(
        [[0, 1, -1],
         [1, 0, -1],
         [1, 1,  1]]
    ) == 5

    assert Solution().cherryPickup(
        [[1, 1, -1],
         [1, -1, 1],
         [-1, 1, 1]]
    ) == 0
