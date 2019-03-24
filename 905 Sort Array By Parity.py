#!/usr/bin/python3
"""
Given an array A of non-negative integers, return an array consisting of all the
even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        pointer
        """
        closed = -1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        return A
