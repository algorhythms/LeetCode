"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is either 0 or 1.
"""
from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, mat: List[List[int]]) -> int:
        """
        01
        11

        01
        10

        000
        001
        110

        brute force
        O(2^N) * O(N^2)

        Each row's pattern is determined by grouping contiguous blocks of identical values. For instance:
        Row [0, 0, 0, 1, 1, 0, 0] produces the pattern: ***|**|**|
        Row [0, 1, 1, 1, 1, 1, 0] produces the pattern: *|*****|*|
        
        The solution is simply the frequency of the most common pattern across all rows in the matrix.
        """
        M = len(mat)
        N = len(mat[0])
        cnt = defaultdict(int)
        mask = (1 << N) - 1
        for i in range(M):
            cur = 0
            for j in range(N):
                cur <<= 1
                cur += mat[i][j]
        
            cnt[cur] += 1
            cnt[(cur ^ mask) & mask] += 1
            
        return max(cnt.values())