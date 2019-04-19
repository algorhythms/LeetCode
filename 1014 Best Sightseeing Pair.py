#!/usr/bin/python3
"""
Given an array A of positive integers, A[i] represents the value of the i-th
sightseeing spot, and two sightseeing spots i and j have distance j - i between
them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the
sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

Example 1:

Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11


Note:
2 <= A.length <= 50000
1 <= A[i] <= 1000
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        """
        Attribute the result to the ending element

        Count the current best score in all previous.
        Distance will increase, then the score will decay
        """
        ret = -float("inf")
        prev_max = A[0]
        for a in A[1:]:
            ret = max(ret, prev_max - 1 + a)
            prev_max = max(prev_max - 1, a)

        return ret

    def maxScoreSightseeingPair_error(self, A: List[int]) -> int:
        """
        brute force O(N^2)

        pre-processing, adjust A[i] as A[i] - i
        error, no direction
        """
        n = len(A)
        B = []
        for i in range(n):
            B.append(A[i] - i)

        # find top 2
        m1, m2 = None, None
        for i in range(n):
            if m1 is None:
                m1 = i
            elif m2 is None:
                m2 = i
            elif B[i] + (i - m1) > B[m1]:
                m1 = i
            elif B[i] + (i - m2) > B[m2]:
                m2 = i
        return A[m2] + A[m1] - abs(m2 - m1)


if __name__ == "__main__":
    assert Solution().maxScoreSightseeingPair([8,1,5,2,6]) == 11
