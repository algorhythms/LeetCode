#!/usr/bin/python3
"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the
data error, one of the numbers in the set got duplicated to another number in
the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error.
Your task is to firstly find the number occurs twice and then find the number
that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/set-mismatch/discuss/113999/C%2B%2B-True-O(1)-space-O(n)-time-(No-input-modifying)-with-clear-explanation
        """
        n = len(nums)
        acc0 = 0  # a ^ b
        for i in range(n):
            acc0 ^= nums[i]
            acc0 ^= i + 1

        first_1 = acc0 & - acc0  # 2's complement, invert the bit left to the first 1 from the right
        # go through the arrays once again and split them in 2 categories, if they have that bit set or not
        # xor them to get a or b
        acc1 = 0
        acc2 = 0
        for i in range(n):
            if nums[i] & first_1:
                acc1 ^= nums[i]
            else:
                acc2 ^= nums[i]

            if (i + 1) & first_1:
                acc1 ^= i + 1
            else:
                acc2 ^= i + 1

        for i in range(n):
            if nums[i] == acc1:
                return [acc1, acc2]

        return [acc2, acc1]
