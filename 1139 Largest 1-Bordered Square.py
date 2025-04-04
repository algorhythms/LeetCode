"""
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
"""
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        """
        111
        101
        111

        brute force, check boarder 

        Reduce from 2D to 1D?

        111
        011
        111
        number of consecutive 1 ending at i, j
        
        then check 4 boarders 
        """
        M = len(grid)
        N = len(grid[0])
        # row 
        R = [
            [0 for _ in range(N+1)]
            for _ in range(M+1)
        ]
        # col
        C = [
            [0 for _ in range(N+1)]
            for _ in range(M+1)
        ]
        for i in range(1, M+1):
            for j in range(1, N+1):
                R[i][j] = R[i][j-1] + 1 if grid[i-1][j-1] == 1 else 0
                C[i][j] = C[i-1][j] + 1 if grid[i-1][j-1] == 1 else 0 
        
        maxa = 0
        # looking at point i, j
        for i in range(M):
            for j in range(N):
                for l in range(1, min(M, N)+1):
                    left = j - l + 1
                    top = i - l + 1
                    if left >= 0 and top >= 0:
                        # print(i, j, left, top)
                        if min(R[i+1][j+1], R[top+1][j+1], C[i+1][j+1], C[i+1][left+1]) >= l:
                            maxa = max(maxa, l)
        
        return maxa * maxa
        