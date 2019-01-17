#!/usr/bin/python3
"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.

The function should return the number of arithmetic slices in the array A.
"""

class Solution:
    def count(self, l):
        return (l-1) * l // 2

    def numberOfArithmeticSlices(self, A):
        """
        Diff the array, find the pattern.
        Find that it is a function of length of the sequence
        With 3 consecutive sequence (l - 1) * l / 2

        :type A: List[int]
        :rtype: int
        """
        ret = 0
        if len(A) < 3:
            return ret

        delta = []
        for i in range(1, len(A)):
            delta.append(A[i] - A[i-1])

        s = 0
        e = 0
        while s < len(delta):
            while e < len(delta) and delta[s] == delta[e]:
                e += 1

            l = e - s
            ret += self.count(l)

            s = e

        return ret


if __name__ == "__main__":
    assert Solution().numberOfArithmeticSlices([1, 2, 3, 4]) == 3
