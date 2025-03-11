#!/usr/bin/python3
"""
You are given a 2D integer array grid with size m x n. You are also given an integer k.

Your task is to calculate the number of paths you can take from the top-left cell (0, 0) to the bottom-right cell (m - 1, n - 1) satisfying the following constraints:

You can either move to the right or down. Formally, from the cell (i, j) you may move to the cell (i, j + 1) or to the cell (i + 1, j) if the target cell exists.
The XOR of all the numbers on the path must be equal to k.
Return the total number of such paths.

Since the answer can be very large, return the result modulo 10^9 + 7.

 

Example 1:

Input: grid = [[2, 1, 5], [7, 10, 0], [12, 6, 4]], k = 11

Output: 3

Explanation: 

The 3 paths are:

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)
(0, 0) → (0, 1) → (1, 1) → (2, 1) → (2, 2)
Example 2:

Input: grid = [[1, 3, 3, 3], [0, 3, 3, 2], [3, 0, 1, 1]], k = 2

Output: 5

Explanation:

The 5 paths are:

(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (2, 1) → (2, 2) → (2, 3)
(0, 0) → (1, 0) → (1, 1) → (1, 2) → (1, 3) → (2, 3)
(0, 0) → (0, 1) → (1, 1) → (1, 2) → (2, 2) → (2, 3)
(0, 0) → (0, 1) → (0, 2) → (1, 2) → (2, 2) → (2, 3)
Example 3:

Input: grid = [[1, 1, 1, 2], [3, 0, 3, 2], [3, 0, 2, 2]], k = 10

Output: 0

 

Constraints:

1 <= m == grid.length <= 300
1 <= n == grid[r].length <= 300
0 <= grid[r][c] < 16
0 <= k < 16
"""
from collections import defaultdict

MOD = int(1e9 + 7)

class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], K: int) -> int:
        """
        DP with a map of counter
        F[i][j] -> dict
        dict: number -> count
        """
        m = len(grid)
        n = len(grid[0])
        F = [
            [defaultdict(int) for _ in range(n)] 
            for _ in range(m)
        ]
        for i in range(m):
            for j in range(n):
                k = grid[i][j]
                if i == 0 and j == 0:
                    F[i][j][k] = 1
                    continue
                
                if i > 0:
                    for v, cnt in F[i-1][j].items():
                        F[i][j][k ^ v] += cnt
                        F[i][j][k ^ v] %= MOD
                if j > 0:
                    for v, cnt in F[i][j-1].items():
                        F[i][j][k ^ v] += cnt
                        F[i][j][k ^ v] %= MOD
        
        return F[~0][~0][K]
