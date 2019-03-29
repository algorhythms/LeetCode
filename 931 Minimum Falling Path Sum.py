#!/usr/bin/python3
"""
Given a square array of integers A, we want the minimum sum of a falling path
through A.

A falling path starts at any element in the first row, and chooses one element
from each row.  The next row's choice must be in a column that is different from
the previous row's column by at most one.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.



Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""
from typing import List
from collections import defaultdict


class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        """
        dp, build from bottom
        let F[i][j] be the min falling path sum at A[i][j]
        using default dict
        """
        m, n = len(A), len(A[0])
        F = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for j in range(n):
            F[m-1][j] = A[m-1][j]

        for i in range(m-2, -1, -1):
            for j in range(n):
                F[i][j] = min(F[i+1][j-1], F[i+1][j], F[i+1][j+1]) + A[i][j]

        return min(
            F[0][j]
            for j in range(n)
        )

    def minFallingPathSum_std(self, A: List[List[int]]) -> int:
        """
        dp, build from bottom
        let F[i][j] be the min falling path sum at A[i][j]
        """
        m, n = len(A), len(A[0])
        F = [[float('inf') for _ in range(n)] for _ in range(m)]
        for j in range(n):
            F[m-1][j] = A[m-1][j]

        for i in range(m-2, -1, -1):
            for j in range(n):
                F[i][j] = min(F[i][j], F[i+1][j] + A[i][j])
                if j - 1 >= 0:
                    F[i][j] = min(F[i][j], F[i+1][j-1] + A[i][j])
                if j + 1 < n:
                    F[i][j] = min(F[i][j], F[i+1][j+1] + A[i][j])

        return min(F[0])


if __name__ == "__main__":
    assert Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 12
