"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


__author__ = 'Daniel'


class Solution(object):
    def isPowerOfFour(self, num):
        """
        Modular calculation
        4^a mod 3
         = (1)^a mod 3
         = 1
        :param num:
        :return:
        """
        if num < 1:
            return False
        if num & num -1 != 0:
            return False

        return num % 3 == 1

    def isPowerOfFourNaive(self, num):
        """
        Naive Determine number of 0 bits to be even
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num & num-1 != 0:
            return False

        while True:
            if num == 0:
                return False
            elif num == 1:
                return True

            num >>= 2