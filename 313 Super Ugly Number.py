# -*- coding: utf-8 -*-
"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For
example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes =
[2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
"""
import heapq
from collections import deque
import sys

__author__ = 'Daniel'


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        DP O(kn)
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        k = len(primes)
        ret = [sys.maxint for _ in xrange(n)]
        ret[0] = 1
        # for each prime, a pointer pointing to the value of next unused number in the result
        idxes = [0 for _ in xrange(k)]
        for i in xrange(1, n):
            for j in xrange(k):
                ret[i] = min(ret[i], primes[j]*ret[idxes[j]])

            for j in xrange(k):
                if ret[i] == primes[j]*ret[idxes[j]]:
                    idxes[j] += 1

        return ret[n-1]


class QueueWrapper(object):
    def __init__(self, idx, q):
        self.idx = idx
        self.q = q

    def __cmp__(self, other):
        return self.q[0] - other.q[0]


class SolutionHeap(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        O(k lg k) + O(nk)
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ret = 1
        h = [QueueWrapper(i, deque([v])) for i, v in enumerate(primes)]
        dic = {e.idx: e for e in h}

        heapq.heapify(h)
        for _ in xrange(n-1):
            mini = heapq.heappop(h)
            ret = mini.q.popleft()
            for i in xrange(mini.idx, len(primes)):
                dic[i].q.append(ret*primes[i])
            heapq.heappush(h, mini)

        return ret

if __name__ == "__main__":
    assert Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]) == 32