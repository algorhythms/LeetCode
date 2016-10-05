"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into
another if and only if both the width and height of one envelope is greater than the width and height of the other
envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4]
=> [6,7]).
"""
import bisect

__author__ = 'Daniel'


class Solution(object):
    def maxEnvelopes(self, A):
        """
        LIS
        binary search

        sort by width first ascending, then sort by height descending (otherwise [3, 3] put in [3, 4]).
        :type A: List[List[int]]
        :rtype: int
        """
        if not A: return 0

        A.sort(key=lambda (w, h): (w, -h))
        F = [-1 for _ in xrange(len(A)+1)]

        F[1] = A[0][1]  # store value rather than index
        k = 1
        for _, h in A[1:]:
            idx = bisect.bisect_left(F, h, 1, k+1)
            F[idx] = h
            k += 1 if idx == k+1 else 0

        return k

    def maxEnvelopesTLE(self, A):
        """
        LIS
        O(n^2)
        :type A: List[List[int]]
        :rtype: int
        """
        if not A: return 0

        predicate = lambda a, b: b[0] > a[0] and b[1] > a[1]
        A.sort()
        n = len(A)
        F = [1 for _ in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if predicate(A[j], A[i]):
                    F[i] = max(F[i], 1 + F[j])

        return max(F)


if __name__ == "__main__":
    assert Solution().maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert Solution().maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]) == 5
