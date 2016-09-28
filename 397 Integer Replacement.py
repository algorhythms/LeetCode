"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
__author__ = 'Daniel'


class Solution(object):
    def integerReplacement(self, n):
        """
        Simulation using dp fails since bi-directional
        Simple recursion

        Math solution: bit manipulation
        https://discuss.leetcode.com/topic/58334/a-couple-of-java-solutions-with-explanations/
        3 is a special case
        :type n: int
        :rtype: int
        """
        ret = 0
        while n != 1:
            ret += 1
            if n & 1 == 0:
                n >>= 1
            elif n == 0b11 or n >> 1 & 1 == 0:
                n -= 1
            else:
                n += 1

        return ret

    def integerReplacementRecur(self, n):
        """
        Simple recursion
        :type n: int
        :rtype: int
        """
        if n == 1: return 0

        ret = 1
        if n%2 == 0:
            ret += self.integerReplacement(n/2)
        else:
            ret += min(self.integerReplacement(n+1), self.integerReplacement(n-1))

        return ret
