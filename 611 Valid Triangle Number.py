#!/usr/bin/python3
"""
Given an array consists of non-negative integers, your task is to count the
number of triplets chosen from the array that can make triangles if we take them
as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        b - a < c < a + b
        Brute force O(n^3)

        3 sums
        Three-pointers
        O(n^2)
        """
        ret = 0
        nums.sort()
        n = len(nums)
        for k in range(n-1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ret += j - i  # move i will always satisfy the constraint
                    j -= 1  # to break
                else:
                    i += 1  # to satisfy

        return ret

    def triangleNumber_error(self, nums: List[int]) -> int:
        """
        b - a < c < a + b
        Brute force O(n^3)

        3 sums
        Three-pointers
        O(n^2)
        """
        ret = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                # error, since move k will not break the formula
                if nums[i] + nums[j] > nums[k]:
                    ret += k - j
                    k -= 1
                else:
                    j += 1

        return ret

    def triangleNumber_slow(self, nums: List[int]) -> int:
        """
        b - a < c < a + b
        Brute force O(n^3)

        Cache + Prune
        """
        cache = {}
        nums.sort()
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) not in cache:
                    cur = 0
                    for k in range(j + 1, n):
                        if nums[k] < nums[i] + nums[j]:
                            cur += 1
                        else:
                            break
                    cache[(i, j)] = cur
                ret += cache[(i, j)]

        return ret


if __name__ == "__main__":
    assert Solution().triangleNumber([2,2,3,4]) == 3
