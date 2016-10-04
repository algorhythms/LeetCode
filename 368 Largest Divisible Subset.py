"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this
subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""
from collections import deque

__author__ = 'Daniel'


class Solution(object):
    def largestDivisibleSubset(self, A):
        """
        Given a divisible subset, when adding a new number, we only needs to validate whether the new number is
        divisible by the largest number in the divisible subset.

        Let F[i] for the size of subset ended with A[i]
        F[i] = max(1 + F[j] if A[i] % A[j] == 0 for j in xrange(i-1))
        pi[i] = argmax(...)
        :type A: List[int]
        :rtype: List[int]
        """
        if not A: return []

        F = {}
        pi = {}
        A.sort()
        for i in xrange(len(A)):
            F[i] = 1
            pi[i] = i
            for j in xrange(i):
                if A[i] % A[j] == 0:
                    if F[i] < 1 + F[j]:
                        F[i] = 1 + F[j]
                        pi[i] = j

        max_i, max_v = 0, 1
        for k, v in F.items():
            if v > max_v:
                max_i, max_v = k, v

        ret = deque()
        cur = max_i
        ret.appendleft(A[cur])
        while pi[cur] != cur:
            cur = pi[cur]
            ret.appendleft(A[cur])

        return list(ret)


if __name__ == "__main__":
    assert Solution().largestDivisibleSubset([1, 2, 4, 8]) == [1, 2, 4, 8]
