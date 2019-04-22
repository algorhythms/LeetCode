#!/usr/bin/python3
"""
Given an integer array A, and an integer target, return the number of tuples
i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Note:

3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""
from typing import List
from collections import defaultdict


MOD = 10 ** 9 + 7


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        """
        Adapted from 3 sum
        3 pointers O(N + K^2)
        j, k scan each element once
        """
        counter = defaultdict(int)
        for a in A:
            counter[a] += 1

        keys = list(counter.keys())
        keys.sort()
        n = len(keys)
        ret = 0
        for i in range(n):
            j = i  # not i + 1
            k = n - 1
            while j <= k:  # not <
                a, b, c = keys[i], keys[j], keys[k]
                if b + c < target - a:
                    j += 1
                elif b + c > target - a:
                    k -= 1
                else:  # equal
                    if a < b < c:
                        ret += counter[a] * counter[b] * counter[c]
                    elif a == b < c:
                        # nC2
                        ret += counter[a] * (counter[a] - 1) // 2 * counter[c]
                    elif a < b == c:
                        ret += counter[a] * counter[b]  * (counter[b] - 1) // 2
                    elif a== b == c:
                        # nC3
                        ret += counter[a] * (counter[a] - 1) * (counter[a] - 2) // (3 * 2)
                    else:
                        raise

                    ret %= MOD
                    j += 1
                    k -= 1

        return ret

    def threeSumMulti_TLE(self, A: List[int], target: int) -> int:
        """
        Adapted from 3 sum
        3 pointers O(N^2)
        j, k scan each element once
        """
        A.sort()
        n = len(A)
        ret = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                if A[j] + A[k] < target - A[i]:
                    j += 1
                elif A[j] + A[k] > target - A[i]:
                    k -= 1
                else:  # equal
                    l_cnt = 1
                    while j + l_cnt < n and A[j + l_cnt] == A[j]:
                        l_cnt += 1

                    r_cnt = 1
                    while k - r_cnt >= 0 and A[k - r_cnt] == A[k]:
                        r_cnt += 1

                    if A[j] != A[k]:
                        ret += l_cnt * r_cnt
                        ret %= MOD
                    else:
                        ret += l_cnt * (l_cnt - 1) // 2  # nC2
                        ret %= MOD

                    j += l_cnt
                    k -= r_cnt

        return ret

    def threeSumMulti_TLE(self, A: List[int], target: int) -> int:
        """
        O(n * target * 3)
        Let F[i][t][k] be the number of k sums using A[:i] to target t
        """
        n = len(A)
        F = [[[0 for _ in range(3 + 1)] for _ in range(target + 1)] for _ in range(n+1)]

        for i in range(n+1):
            F[i][0][0] = 1

        for i in range(1, n + 1):
            for t in range(target + 1):
                for k in range(1, 3 + 1):
                    # choose A[i-1] or not
                    F[i][t][k] = F[i-1][t][k] % MOD
                    if t - A[i-1] >= 0:
                        F[i][t][k] += F[i-1][t-A[i-1]][k-1] % MOD

        print(F[n][target][3])
        return F[n][target][3]

    def threeSumMulti_TLE(self, A: List[int], target: int) -> int:
        """
        O(n * target * 3)
        Let F[i][t][k] be the number of k sums using A[:i] to target t
        """
        F = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        n = len(A)
        for i in range(n+1):
            F[i][0][0] = 1

        for i in range(1, n + 1):
            for t in range(target + 1):
                for k in range(1, 3 + 1):
                    # choose A[i-1] or not
                    F[i][t][k] = F[i-1][t][k] + F[i-1][t-A[i-1]][k-1]
                    F[i][t][k] %= MOD

        return F[n][target][3]


if __name__ == "__main__":
    assert Solution().threeSumMulti([1,1,2,2,3,3,4,4,5,5], 8) == 20
