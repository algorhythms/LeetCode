"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
"""
__author__ = 'Daniel'


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

def guess(num):
    return -1


class Solution(object):
    def guessNumber(self, n):
        """
        Binary search, transform [1, n] into [1, n+1), to make sure the loop is making progress
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n+1
        while True:
            mid = (lo + hi) / 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 1:
                hi = mid
            else:
                lo = mid + 1
