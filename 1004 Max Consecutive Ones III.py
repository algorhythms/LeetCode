#!/usr/bin/python3
"""
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s.



Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation:
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.
Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation:
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.


Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
"""
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        """
        len(gap)
        But there is multiple gap need to fill, and which gaps to fill is
        undecided. Greedy? No. DP?

        Sliding Window: Find the longest subarray with at most K zeros.
        """
        i, j = 0, 0
        cnt_0 = 0
        n = len(A)
        ret = 0
        while i < n and j < n:
            while j < n:
                if A[j] == 0 and cnt_0 < K:
                    j += 1
                    cnt_0 += 1
                elif A[j] == 1:
                    j += 1
                else:
                    break

            ret = max(ret, j - i)
            if A[i] == 0:
                cnt_0 -= 1
            i += 1

        return ret


if __name__ == "__main__":
    assert Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
