#!/usr/bin/python3
"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i]
stones.

A move consists of merging exactly K consecutive piles into one pile, and the
cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is
impossible, return -1.



Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation:
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't
merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation:
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.


Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""
from typing import List
from functools import lru_cache


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        """
        Mergeable? K -> 1. Reduction size (K - 1)
        N - (K - 1) * m = 1
        mergeable: (N - 1) % (K - 1) = 0

        K consecutive
        every piles involves at least once
        Non-consecutive: priority queue merge the least first
        But here it is consecutive, need to search, cannot gready

        * Merge the piles cost the same as merge individual ones.

        Attemp 1:
        F[i] = cost to merge A[:i] into 1
        F[i] = F[i-3] + A[i-1] + A[i-2] + A[i-3] ??

        Attemp 2:
        F[i][j] = cost of merge A[i:j] into 1
        F[i][j] = F[i][k] + F[k][j] ??

        Answer:
        F[i][j][m] = cost of merge A[i:j] into m piles
        F[i][j][1] = F[i][j][k] + sum(stones[i:j])  # merge 
        F[i][j][m] = min F[i][mid][1] + F[mid][j][m-1]  # add

        initial:
        F[i][i+1][1] = 0
        F[i][i+1][m] = inf

        since the mid goes through the middle in the i, j.
        Use memoization rather than dp
        """
        N = len(stones)
        sums = [0]
        for s in stones:
            sums.append(sums[-1] + s)

        @lru_cache(None)
        def F(i, j, m):
            if i >= j or m < 1:
                return float("inf")

            n = j - i
            if (n - m) % (K - 1) != 0:
                return float("inf")

            if j == i + 1:
                if m == 1:
                    return 0
                return float("inf")

            if m == 1:
                return F(i, j, K) + sums[j] - sums[i]

            ret = min(
                F(i, mid, 1) + F(mid, j, m - 1)
                for mid in range(i + 1, j, K - 1)
            )
            return ret

        ret = F(0, N, 1)
        return ret if ret != float("inf") else -1


if __name__ == "__main__":
    assert Solution().mergeStones([3,5,1,2,6], 3) == 25
