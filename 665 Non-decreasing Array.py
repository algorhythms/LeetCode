#!/usr/bin/python3
"""
Given an array with n integers, your task is to check if it could become
non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every
i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
"""
from typing import List


class Solution:
    def checkPossibility(self, A: List[int]) -> bool:
        """
        greedy change
        two way of changing
        """
        changed = False
        for i in range(len(A) - 1):
            if A[i] <= A[i + 1]:
                continue
            if not changed:
                if i - 1 < 0 or A[i-1] <= A[i+1]:
                    A[i] = A[i+1]
                else:
                    A[i+1] = A[i]
                changed = True
            else:
                return False

        return True

    def checkPossibility_error(self, A: List[int]) -> bool:
        """
        greedy change
        """
        changed = False
        for i in range(len(A) - 1):
            if A[i] <= A[i + 1]:
                continue
            if not changed:
                A[i] = A[i + 1]  # Error
                if i - 1 < 0 or A[i - 1] <= A[i]:
                    changed = True
                else:
                    return False
            else:
                return False

        return True


if __name__ == "__main__":
    assert Solution().checkPossibility([4,2,3]) == True
    assert Solution().checkPossibility([3,4,2,3]) == False
    assert Solution().checkPossibility([2,3,3,2,4]) == True
