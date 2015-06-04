"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it
will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""
__author__ = 'Daniel'


class Solution:
    def rob(self, nums):
        """
        DP
        O(n)
        f_i = max(f_{i-1}, f_{i-2} + A[i]
        """
        n = len(nums)
        f = [0 for _ in xrange(n+2)]
        for i in xrange(2, n+2):
            f[i] = max(
                f[i-1],
                f[i-2] + nums[i-2]
            )

        return f[-1]





