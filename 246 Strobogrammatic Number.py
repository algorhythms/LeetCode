"""
Premium Question
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
        """

        :type num: str
        :rtype: bool
        """
        num = list(num)
        rev = []
        for digit in reversed(num):
            try:
                rev.append(self.map[digit])
            except KeyError:
                return False

        return num == rev