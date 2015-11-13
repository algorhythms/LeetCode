"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
import math

__author__ = 'Danyang'


class Solution(object):
    def numTrees_math(self, n):
        """
        number of unique binary search tree
        Catalan Number

        C_n = {2n\choose n} - {2n\choose n+1}
        Proof: http://en.wikipedia.org/wiki/Catalan_number#Second_proof
        :param n: integer
        :return: integer
        """
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n))-math.factorial(2*n)/(
            math.factorial(n+1)*math.factorial(n-1))

    def numTrees(self, n):
        """
        number of unique binary search tree
        dp

        dp[i] means # BST constructed from [1...i]

        dp[3] = dp[0]*dp[2]  # 1 as pivot
               +dp[1]*dp[1]  # 2 is pivot
               +dp[2]*dp[0]  # 3 as pivot

        follow the 2nd proof of Catalan number.
        Proof: http://en.wikipedia.org/wiki/Catalan_number#First_proof
        :param n: integer
        :return: integer
        """
        if n < 2:
            return n

        dp = [0 for _ in xrange(n+1)]
        dp[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]


if __name__ == "__main__":
    assert Solution().numTrees(100) == Solution().numTrees_math(100)