# -*- coding: utf-8 -*-
"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are
asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
__author__ = 'Daniel'


class Solution(object):
    def maxCoins(self, A):
        """
        Divide & Conquer <- Divide Boundary <- Reverse Thinking

        Let F[i][j] be the max scores burst all over A[i:j]
        F[i][j] = max(F[i][k] + A[i-1]*A[k]*A[j] + F[k+1][j] \forall k) where k is the last one to burst.

        Reference: https://leetcode.com/discuss/72216/share-some-analysis-and-explanations?show=72358#c72358
        :type A: List[int]
        :rtype: int
        """
        n = len(A)

        def get(i):
            if i < 0 or i >= n: return 1
            return A[i]

        F = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
        for i in xrange(n+1, -1, -1):
            for j in xrange(i+1, n+1):
                F[i][j] = max(
                    F[i][k]+get(i-1)*get(k)*get(j)+F[k+1][j]
                    for k in xrange(i, j)
                )

        return max(map(max, F))


if __name__ == "__main__":
    assert Solution().maxCoins([3, 1, 5, 8]) == 167

