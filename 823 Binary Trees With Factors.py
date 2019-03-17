#!/usr/bin/python3
"""
Given an array of unique integers, each integer is strictly greater than 1.

We make a binary tree using these integers and each number may be used for any
number of times.

Each non-leaf node's value should be equal to the product of the values of it's
children.

How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

Example 1:

Input: A = [2, 4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: A = [2, 4, 5, 10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2],
[10, 2, 5], [10, 5, 2].

Note:

1 <= A.length <= 1000.
2 <= A[i] <= 10 ^ 9.
"""
from typing import List


MOD =  10 ** 9 + 7


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        """
        Let F[i] be the number of factored binary tree rooted at i
        """
        A.sort()
        F = {}
        for i in range(len(A)):
            F[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in F:
                    F[A[i]] += F[A[j]] * F[A[i] // A[j]]  # #left * #right
                    F[A[i]] %= MOD

        return sum(F.values()) % MOD
