#!/usr/bin/python3
"""
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2]
< nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Median + 3-way partitioning
        """
        n = len(nums)
        # mid = self.find_kth(nums, 0, n, (n - 1) // 2)
        # median = nums[mid]
        median = list(sorted(nums))[n//2]

        # three way pivot
        odd = 1
        even = n - 1 if (n - 1) % 2 == 0 else n - 2
        i = 0
        while i < n:
            if nums[i] < median:
                if i >= even and i % 2 == 0:
                    i += 1
                    continue
                nums[i], nums[even] = nums[even], nums[i]
                even -= 2

            elif nums[i] > median:
                if i <= odd  and i % 2 == 1:
                    i += 1
                    continue
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2
            else:
                i += 1

    def find_kth(self, A, lo, hi, k):
        p = self.pivot(A, lo, hi)
        if k == p:
            return p
        elif k > p:
            return self.find_kth(A, p + 1, hi, k)
        else:
            return self.find_kth(A, lo, p, k)

    def pivot(self, A, lo, hi):
        # need 3-way pivot, otherwise TLE
        p = lo
        closed = lo
        for i in range(lo + 1, hi):
            if A[i] < A[p]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[p] = A[p], A[closed]
        return closed


if __name__ == "__main__":
    Solution().wiggleSort([1, 5, 1, 1, 6, 4])
