#!/usr/bin/python3
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""


class Solution:
    def findDisappearedNumbers(self, A):
        """
        You can use hash map with extra space O(n).
        To use without extra space, notice the additional constraints that:
            1. 1 ≤ a[i] ≤ n
            2. appear twice or once
        => use original array as storage with a[i] (- 1) as the index
        :type A: List[int]
        :rtype: List[int]
        """
        for idx in range(len(A)):
            while True:
                target = A[idx] - 1
                if idx == target or A[idx] == A[target]:
                    break 
                A[idx], A[target] = A[target], A[idx]

        missing = []
        for idx, elm in enumerate(A):
            if idx != elm - 1:
                missing.append(idx + 1)
        return missing


if __name__ == "__main__":
    assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
