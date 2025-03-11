"""
You are given a string source of size n, a string pattern that is a 
subsequence
 of source, and a sorted integer array targetIndices that contains distinct numbers in the range [0, n - 1].

We define an operation as removing a character at an index idx from source such that:

idx is an element of targetIndices.
pattern remains a 
subsequence
 of source after removing the character.
Performing an operation does not change the indices of the other characters in source. For example, if you remove 'c' from "acb", the character at index 2 would still be 'b'.

Return the maximum number of operations that can be performed.

 

Example 1:

Input: source = "abbaa", pattern = "aba", targetIndices = [0,1,2]

Output: 1

Explanation:

We can't remove source[0] but we can do either of these two operations:

Remove source[1], so that source becomes "a_baa".
Remove source[2], so that source becomes "ab_aa".
Example 2:

Input: source = "bcda", pattern = "d", targetIndices = [0,3]

Output: 2

Explanation:

We can remove source[0] and source[3] in two operations.

Example 3:

Input: source = "dda", pattern = "dda", targetIndices = [0,1,2]

Output: 0

Explanation:

We can't remove any character from source.

Example 4:

Input: source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4]

Output: 2

Explanation:

We can remove source[2] and source[3] in two operations.

 

Constraints:

1 <= n == source.length <= 3 * 10^3
1 <= pattern.length <= n
1 <= targetIndices.length <= n
targetIndices is sorted in ascending order.
The input is generated such that targetIndices contains distinct elements in the range [0, n - 1].
source and pattern consist only of lowercase English letters.
The input is generated such that pattern appears as a subsequence in source.
"""
import sys


class Solution:
    def maxRemovals_backward(self, A: str, B: str, targetIndices: List[int]) -> int:
        """
        Max possiblee: Remove all targetIndices, check pattern

        Sorted array of targetIndices
        From pattern, map from pattern idx -> list of source idx 

        Check subsequence - two pointers

        Backward (bottom right) DP
        Define source as A and pattern as B
        Let F[i][j] be the max operation for A[i:] and B[j:] while satisfy the condition 
        F[i][j] =
         * F[i+1][j] + 1  # remove A[i]
         * F[i+1][j+1]  # A[i] == B[j] matching, no removal
        """
        target = set(targetIndices)
        m = len(A)
        n = len(B)
        F = [
            [-sys.maxsize-1 for _ in range(n+1)]
            for _ in range(m+1)
        ]
        F[m][n] = 0
        for i in range(m-1, -1, -1):
            F[i][n] = F[i+1][n] + (1 if i in target else 0)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                F[i][j] = F[i+1][j] + (1 if i in target else 0)  # remove A[i]
                if A[i] == B[j]:
                    F[i][j] = max(F[i][j], F[i+1][j+1])  # match A[i] B[j]
        
        return F[0][0]

    def maxRemovals(self, A: str, B: str, targetIndices: List[int]) -> int:
        """
        Forward (top left) DP
        Define source as A and pattern as B
        Let F[i][j] be the max operation for A[:i] and B[:j] while satisfy the condition 
        F[i][j] =
         * F[i-1][j] + 1  # remove A[i-1]
         * F[i-1][j-1]  # A[i] == B[j] matching, no removal
        """
        target = set(targetIndices)
        m = len(A)
        n = len(B)
        F = [
            [-sys.maxsize-1 for _ in range(n+1)]
            for _ in range(m+1)
        ]
        F[0][0] = 0
        for i in range(1, m+1):
            F[i][0] = F[i-1][0] + (1 if i-1 in target else 0)

        for i in range(1, m+1):
            for j in range(1, n+1):
                F[i][j] = F[i-1][j] + (1 if i-1 in target else 0)  # remove A[i]
                if A[i-1] == B[j-1]:
                    F[i][j] = max(F[i][j], F[i-1][j-1])  # match A[i] B[j]
        
        return F[m][n]

