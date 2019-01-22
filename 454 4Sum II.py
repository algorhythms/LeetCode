#!/usr/bin/python3
"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where
0 ≤ N ≤ 500. All integers are in the range of -2^28 to 2^28 - 1 and the result
is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from collections import defaultdict


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        Brute force with map: O(N^3)

        O(N^3) is pretty large, O(N^2) or O(N log N)?

        O(N^2) to sum cartesian product (A, B) to construct index
        similar to C, D.

        Then index loop up
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        AB = defaultdict(int)
        CD = defaultdict(int)
        for i in range(N):
            for j in range(N):
                AB[A[i] + B[j]] += 1
                CD[C[i] + D[j]] += 1

        ret = 0
        # O(N^2)
        for gross, count in AB.items():
            target = 0 - gross
            ret += count * CD[target]

        return ret


if __name__ == "__main__":
    A = [ 1, 2]
    B = [-2,-1]
    C = [-1, 2]
    D = [ 0, 2]
    assert Solution().fourSumCount(A, B, C, D) == 2
