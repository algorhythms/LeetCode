#!/usr/bin/python3
"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

The function should return the number of arithmetic subsequence slices in the
array A. (Subsequence rather than slide)
"""
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        Subsequence, count the number, looks like dp
        use defaultdict for easy dp array construction

        D[i][d] stores the number of arithmetic subsequence ending at A[i], with
        delta d

        result would be
        sum(
            D[i][d]
            if >= 3 consecutive subsequence A[i], A[j], A[k] ...
            for some j, k
        )

        summing D[j][d] rather than D[i][d] since we need >= 3 subsequence and
        D[i][d] contains the length 2.

        This approach cannot be extended to >= 4 subsequence
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        D = defaultdict(lambda: defaultdict(int))
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                D[i][d] += 1 + D[j][d]
                if D[j][d] > 0:
                    # >= 3 subsequence with A[k], A[j], A[i]
                    ret += D[j][d]  # not D[i][d]

        return ret

    def numberOfArithmeticSlices_error(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        D = defaultdict(lambda: defaultdict(int))
        for i in range(len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                D[i][delta] += 1 + D[j][delta]

            for j in range(i):
                delta = A[i] - A[j]
                if D[j][delta] > 0:
                    ret += D[i][delta]  # counted the length 2

        return ret


if __name__ == "__main__":
    assert Solution().numberOfArithmeticSlices([2, 4, 6, 8, 10]) == 7
