#!/usr/bin/python3
"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then
our score is the sum of the average of each group. What is the largest score we
can achieve?

Note that our partition must use every number in A, and that scores are not
necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is
9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
"""
from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        """
        Memoized Backtracking + Prefix sum
        My first hunch is correct
        Complexity O(N^2 * K), mark sum and different way of forming groups
        (inserting dividers)

        calculating each F[l, k] will need O(N) time, thus total O(n^2 k)
        """
        n = len(A)
        prefix_sum = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]

        F = {}
        self.dfs(A, n, prefix_sum, F, K)
        return F[n, K]

    def dfs(self, A, l, prefix_sum, F, k):
        """
        dfs search divide
        make A[:l] k groups
        """
        if l < k:
            return -float('inf')

        if (l, k) not in F:
            if k == 1:
                ret = prefix_sum[l] / l
            else:
                n = len(A)
                ret = -float('inf')
                for j in range(l-1, -1, -1):
                    trail = (prefix_sum[l] - prefix_sum[j]) / (l - j)
                    ret = max(
                        ret,
                        self.dfs(A, j, prefix_sum, F, k-1) + trail
                    )

            F[l, k] = ret

        return F[l, k]

    def dfs_error(self, A, i, prefix_sum, F, k):
        """
        inconvenient

        dfs search divide
        make A[:i] 1 group
        make A[i:] k - 1 group
        """
        if (i, k) not in F:
            ret = 0
            avg = prefix_sum[i] / i
            ret += avg
            ret += max(
                # error
                self.dfs(A, j, prefix_sum, F, k - 1)
                for j in range(i, len(A))
            )
            F[i, k] = ret

        return F[i, k]


if __name__ == "__main__":
    assert Solution().largestSumOfAverages([9,1,2,3,9], 3) == 20
