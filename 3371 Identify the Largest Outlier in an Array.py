#!/usr/bin/python3
"""
You are given an integer array nums. This array contains n elements, where exactly n - 2 elements are special numbers. One of the remaining two elements is the sum of these special numbers, and the other is an outlier.

An outlier is defined as a number that is neither one of the original special numbers nor the element representing the sum of those numbers.

Note that special numbers, the sum element, and the outlier must have distinct indices, but may share the same value.

Return the largest potential outlier in nums.

Example 1:

Input: nums = [2,3,5,10]

Output: 10

Explanation:

The special numbers could be 2 and 3, thus making their sum 5 and the outlier 10.

Example 2:

Input: nums = [-2,-1,-3,-6,4]

Output: 4

Explanation:

The special numbers could be -2, -1, and -3, thus making their sum -6 and the outlier 4.

Example 3:

Input: nums = [1,1,1,1,1,5,5]

Output: 5

Explanation:

The special numbers could be 1, 1, 1, 1, and 1, thus making their sum 5 and the other 5 as the outlier.

Constraints:

3 <= nums.length <= 105
-1000 <= nums[i] <= 1000
The input is generated such that at least one potential outlier exists in nums.
"""
import sys
from collections import defaultdict
from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        if remove outlier, what will be the value of array sum
        """
        total = sum(nums)
        hm = defaultdict(list)
        for i, v in enumerate(nums):
            hm[v].append(i)
        
        maxa = -sys.maxsize-1
        for v in nums:
            remain = total - v
            if remain % 2 == 0:
                half = remain // 2
                if half == v and len(hm[half]) == 1:
                    continue 
                if half in hm:
                    maxa = max(maxa, v)
        
        return maxa
