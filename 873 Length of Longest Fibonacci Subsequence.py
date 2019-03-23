#!/usr/bin/python3
"""
A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence,
find the length of the longest fibonacci-like subsequence of A.  If one does not
exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any
number of elements (including none) from A, without changing the order of the
remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)



Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].


Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)
"""
from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
            """
            F[i][j] longest fib subsequence ending at A[i] with 2nd last element
            A[j]

            F[k][i] = F[i][j] + 1 if A[i] + A[j] = A[k]

            O(N^2) * O(N) = O(N^3)

            can be optimized to O(N^2) by look forward
            """
            n = len(A)
            F = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                F[i][i] = 1
                for j in range(i):
                    F[i][j] = 2

            idxes = {}
            for i in range(n):
                idxes[A[i]] = i

            for i in range(n):
                for j in range(i):
                    Ak = A[i] + A[j]
                    if Ak in idxes:
                        k = idxes[Ak]
                        F[k][i] = max(F[k][i], F[i][j] + 1)

            return max(
                F[i][j] if F[i][j] > 2 else 0
                for i in range(n)
                for j in range(i)
            )

    def lenLongestFibSubseq_TLE(self, A: List[int]) -> int:
        """
        F[i][j] longest fib subsequence ending at A[i] with 2nd last element
        A[j]

        F[k][i] = F[i][j] + 1 if A[i] + A[j] = A[k]

        O(N^2) * O(N) = O(N^3)

        can be optimized to O(N^2) by look forward
        """
        n = len(A)
        F = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            F[i][i] = 1
            for j in range(i):
                F[i][j] = 2

        for k in range(n):
            for i in range(k):
                for j in range(i):
                    if A[i] + A[j] == A[k]:
                        F[k][i] = max(F[k][i], F[i][j] + 1)

        return max(
            F[i][j] if F[i][j] > 2 else 0
            for i in range(n)
            for j in range(i)
        )

if __name__ == "__main__":
    assert Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]) == 5
