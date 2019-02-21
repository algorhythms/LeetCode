#!/usr/bin/python3
"""
Given a sorted array, two integers k and x, find the k closest elements to x in
the array. The result should also be sorted in ascending order. If there is a
tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
"""
from typing import List
from bisect import bisect_left
from collections import deque


class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        """
        binary search without two pointers scanning
        """
        n = len(A)
        lo = 0
        hi = n - k
        while lo < hi:
            mid = (lo + hi) // 2
            if abs(x - A[mid]) > abs(A[mid + k] - x):
                # better to have A[mid+k] rather than A[mid]
                lo = mid + 1
            else:
                hi = mid

        return A[lo:lo+k]

    def findClosestElements2(self, A: List[int], k: int, x: int) -> List[int]:
        """
        input sorted arrya
        two pointers
        """
        n = len(A)
        idx = bisect_left(A, x)
        ret = deque()
        i = idx - 1
        j = idx
        while k:
            if 0 <= i < n and 0 <= j < n:
                if abs(A[i] - x) <= abs(A[j] - x):
                    ret.appendleft(A[i])
                    i -= 1
                else:
                    ret.append(A[j])
                    j += 1
            elif 0 <= i < n:
                ret.appendleft(A[i])
                i -= 1
            elif 0 <= j < n:
                ret.append(A[j])
                j += 1
            else:
                raise

            k -= 1

        return list(ret)


if __name__ == "__main__":
    assert Solution().findClosestElements([1,2,3,4,5], 4, 3) == [1,2,3,4]
    assert Solution().findClosestElements([1,2,3,4,5], 4, -1) == [1,2,3,4]
