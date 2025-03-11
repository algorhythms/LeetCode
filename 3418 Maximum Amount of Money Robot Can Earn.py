"""
You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:

If coins[i][j] >= 0, the robot gains that many coins.
If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

 

Example 1:

Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

Output: 8

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 0 coins (total coins = 0).
Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).
Example 2:

Input: coins = [[10,10,10],[10,10,10]]

Output: 40

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 10 coins (total coins = 10).
Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).
 

Constraints:

m == coins.length
n == coins[i].length
1 <= m, n <= 500
-1000 <= coins[i][j] <= 1000
"""
import sys


class Solution:
    def maximumAmount_error(self, M: List[List[int]]) -> int:
        """
        Let F[i][j][k] be the max amount at M[i-1][j-1] with k-1 number of neutralization 

        F[i][j][k] = max(
            F[i-1][j][k] + M[i-1][j-1],
            F[i][j-1][k] + M[i-1][j-1],
            F[i-1][j][k-1],
            F[i][j-1][k-1],
        )
        """
        m = len(M)
        n = len(M[0])
        F = [
            [
                [
                    0 
                    for _ in range(4)  # error here
                ] 
                for _ in range(n+1)
            ]
            for _ in range(m+1)
        ]
        for i in range(m+1):
            for j in range(n+1):
                F[i][j][0] = -sys.maxsize-1
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(1, 4):
                    F[i][j][k] = max(
                        F[i-1][j][k] + M[i-1][j-1],
                        F[i][j-1][k] + M[i-1][j-1],
                        F[i-1][j][k-1],
                        F[i][j-1][k-1],
                    )

        return max(F[m][n])

    def maximumAmount(self, M: List[List[int]]) -> int:
        """
        Let F[i][j][k] be the max amount at M[i-1][j-1] with k-1 number of neutralization 

        F[i][j][k] = max(
            F[i-1][j][k] + M[i-1][j-1],
            F[i][j-1][k] + M[i-1][j-1],
            F[i-1][j][k-1],
            F[i][j-1][k-1],
        )
        """
        m = len(M)
        n = len(M[0])
        F = [
            [
                [
                    -sys.maxsize-1 
                    for _ in range(4)
                ]
                for _ in range(n+1)
            ]
            for _ in range(m+1)
        ]
        # prepare for M[0][0]
        F[0][1][1] = 0
        F[1][0][1] = 0
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                for k in range(1, 4):
                    F[i][j][k] = max(
                        F[i-1][j][k] + M[i-1][j-1],
                        F[i][j-1][k] + M[i-1][j-1],
                        F[i-1][j][k-1],
                        F[i][j-1][k-1],
                    )
        return max(F[m][n])
