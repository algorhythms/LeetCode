"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate
between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with
fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and
negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two
differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is
obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining
elements in their original order.
"""
__author__ = 'Daniel'


class Solution(object):
    def wiggleMaxLength(self, A):
        """
        Let H[i] be max wiggle length for [0, i] with A[i] as high point
        Let L[i] be similarly defined but as low point.

        Consider A[i] > A[i-1]:
          H[i] = L[i-1] + 1 # wiggle up
          L[i] = L[i-1]  #
        A[i] < A[i-1] case has similar formula

          H[i] = H[i-1]
               = L[i-1] + 1

          L[i] = L[i-1]
               = H[i-1] + 1

        Therefore, max(H[i], L[i]) are monotonously non-decreasing  (rather than H[i] or L[i] monotonously
        non-decreasing separately.
        O(n)

        Additionally, possibly space optimized to O(1) by reusing space
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        N = len(A)
        H = [1 for _ in xrange(N)]
        L = [1 for _ in xrange(N)]
        for i in xrange(1, N):
            L[i] = H[i-1] + 1 if A[i] < A[i-1] else L[i-1]
            H[i] = L[i-1] + 1 if A[i] > A[i-1] else H[i-1]

        return max(H[N-1], L[N-1])

    def wiggleMaxLengthSuboptimal(self, A):
        """
        Let H[i] be wiggle length ends at i, with A[i] as high point
        Let L[i] be similarly defined but as low point.
        O(n^2)
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0

        N = len(A)
        H = [1 for _ in xrange(N)]
        L = [1 for _ in xrange(N)]
        gmax = 1
        for i in xrange(1, N):
            for j in xrange(i):
                if A[i] > A[j]:
                    H[i] = max(H[i], L[j] + 1)
                elif A[i] < A[j]:
                    L[i] = max(L[i], H[j] + 1)

                gmax = max(gmax, H[i], L[i])

        return gmax
