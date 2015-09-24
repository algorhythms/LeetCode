"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class TwoSum(object):
    def __init__(self):
        """
        initialize your data structure here
        """
        self.hash_map = defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.hash_map[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        return any(
            value-k in self.hash_map and (value-k != k or self.hash_map[k] > 1)
            for k in self.hash_map
        )

    def find_TLE(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for k in self.hash_map.keys():
            target = value - k
            if target in self.hash_map and (target != k or self.hash_map[target] > 1):
                return True

        return False
