"""
Given an m x n binary matrix mat, return the number of submatrices that have all ones.

Example 1:

Input: mat = [
    [1,0,1],
    [1,1,0],
    [1,1,0]
]
Output: 13
Explanation: 
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation: 
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
 

Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        1-D 1-submatrix: 
        [1, 0, 1, 1, 1]
        Let F[j] be number of 1-submatrix ending AT j-1

        F[j] = F[j] + 1 if F[j-1] == 1 
               0        otherwise
        In the end, sum(F)

        2-D submatrix:
        [1, 0, 1, 1, 1]
        [1, 1, 0, 1, 1]
        Consider a 2-row matrix, Project 2D into 1D:
        [1, 0, 0, 1, 1]
        """
        ret = 0
        M = len(mat)
        N = len(mat[0])
        for lo in range(M):
            # is all ones for mat[lo:hi][j]
            is_ones_col = [True for j in range(N)] 
            for hi in range(lo+1, M+1):
                for j in range(N):
                    is_ones_col[j] &= mat[hi-1][j]  # mem saving

                F = [0 for _ in range(N+1)]
                for j in range(1, N+1):
                    F[j] = F[j-1] + 1 if is_ones_col[j-1] else 0 
                    ret += F[j]
        
        return ret