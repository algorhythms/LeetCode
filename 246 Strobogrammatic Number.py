"""
Premium Question
Checking Strobogrammatic
https://leetcode.com/problems/strobogrammatic-number/
"""
__author__ = 'Daniel'


class Solution:
    def __init__(self):
        self.map = {
            "1": "1",
            "6": "9",
            "9": "6",
            "8": "8",
            "0": "0"
        }

    def isStrobogrammatic(self, num):
        for i in xrange(len(num)/2+1):
            if num[i] not in self.map or self.map[num[i]] != num[len(num)-1-i]:
                return False

        return True

    def isStrobogrammatic_tedious(self, num):
        """

        :type num: str
        :rtype: bool
        """
        num = list(num)
        rev = []  # reverse
        for digit in reversed(num):
            try:
                rev.append(self.map[digit])
            except KeyError:
                return False

        return num == rev