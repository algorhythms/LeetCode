"""
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 10^9 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^7
"""
import sys


MOD = int(1e9+7)


class Solution:
    def maxSumMinProduct(self, A: List[int]) -> int:
        """
        min(A[i:j]) * sum(A[i:j])
        shrink i, j will make min larger while sum smaller
        sum can be get in O(1) by prefix sum
        min(A[i:j]) is O(1) by keeping track of min when iterating j
        O(N^2)

        Can we do in O(N) by some two pointers?

        Can we find the maximum min-product for every value in the array?
        For every value, find the next smaller on the right, and similarly on the left
        """
        N = len(A)
        P = [0 for _ in range(N+1)]  # prefix sum of A[:i]
        for i in range(1, N+1):
            P[i] = P[i-1] + A[i-1]

        R = [N for _ in range(N)]  # next smaller on right 
        # monotonic increasing stack, storing pending candidate that have not found the next smaller element, 
        # til monotonicity break, pop and process it 
        stk = []
        for i in range(N):
            while stk and A[stk[~0]] > A[i]:
                t = stk.pop()
                R[t] = i
            stk.append(i)
        
        L = [-1 for _ in range(N)]  # next smaller on the left
        for i in range(N-1, -1, -1):
            while stk and A[stk[~0]] > A[i]:
                t = stk.pop()
                L[t] = i
            stk.append(i)

        maxa = -sys.maxsize-1
        for i in range(N):
            l = L[i]
            r = R[i]
            # sum(A[l+1:r])
            s = P[r] - P[l+1]
            maxa = max(maxa, s * A[i])
        
        return maxa % MOD
   