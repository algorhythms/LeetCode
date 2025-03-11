"""
You are given an m x n binary matrix grid and an integer health.

You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).

You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.

Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.

Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.

 

Example 1:

Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.


Example 2:

Input: grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3

Output: false

Explanation:

A minimum of 4 health points is needed to reach the final cell safely.


Example 3:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5

Output: true

Explanation:

The final cell can be reached safely by walking along the gray cells below.



Any path that does not go through the cell (1, 1) is unsafe since your health will drop to 0 when reaching the final cell.

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
2 <= m * n
1 <= health <= m + n
grid[i][j] is either 0 or 1.
"""
import heapq
import sys 


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        """
        F[i][j] maximum health at i, j
        But four directions, not monotonic, DP may not work
        visited to avoid loop

        Greedy visited 0 with heap. 
        N = m*n 
        O(N log N)
        """
        m = len(grid)
        n = len(grid[0])
        F = [
            [sys.maxsize for _ in range(n)]
            for _ in range(m)
        ]
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        h = [(grid[0][0], 0, 0)]  # heap queue of (acc, i, j)
        while h:
            acc, i, j = heapq.heappop(h)
            for di, dj in dirs:
                I = i + di
                J = j + dj
                if 0 <= I < m and 0 <= J < n:
                    nxt = acc + grid[I][J]
                    if F[I][J] > nxt:
                        F[I][J] = nxt
                        heapq.heappush(h, (nxt, I, J))
        
        return F[~0][~0] < health
        