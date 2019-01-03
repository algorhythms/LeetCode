#!/usr/bin/python3
"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.
"""


class Solution:
    def arrangeCoins(self, n):
        """
        Solve a math equation
        (1+r)r/2 <= n
        :type n: int
        :rtype: int
        """
        return int(
            (2*n + 1/4)**(1/2)  - 1/2
        )


if __name__ == "__main__":
    assert Solution().arrangeCoins(5) == 2
    assert Solution().arrangeCoins(8) == 3
