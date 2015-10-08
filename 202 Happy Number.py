"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""
__author__ = 'Daniel'


class Solution:
    def isHappy(self, n):
        """
        Start with several simple cases and find the pattern.

        if converge to 1, return True
        if loop, return False
        :param n:
        :rtype: bool
        """
        nxt = 0
        appeared = set()
        while True:
            nxt += (n%10)*(n%10)
            n /= 10
            if n == 0:
                if nxt == 1:
                    return True
                if nxt in appeared:
                    return False

                appeared.add(nxt)
                n = nxt
                nxt = 0

