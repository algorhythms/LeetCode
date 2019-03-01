#!/usr/bin/python3
"""
Given two integer arrays A and B, return the maximum length of an subarray that
appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
from typing import List
from collections import defaultdict


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
        similar to longest substring
        Brute force O(mn)

        DP - O(mn)
        possible
        F[i][j] be the longest substring ended at A[i-1], B[i-1]
        F[i][j] = F[i-1][j-1] + 1 if A[i-1] == B[i-1] else 0
        """
        m, n = len(A), len(B)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    F[i][j] = F[i-1][j-1] + 1

        return max(
            F[i][j]
            for i in range(1, m+1)
            for j in range(1, n+1)
        )


if __name__ == "__main__":
    assert Solution().findLength([1,2,3,2,1], [3,2,1,4,7]) == 3
