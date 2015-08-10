"""
Premium Question
"""
import sys
from bisect import bisect_left

__author__ = 'Daniel'


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        lst1 = [i for i, v in enumerate(words) if v == word1]
        lst2 = [i for i, v in enumerate(words) if v == word2]
        mini = sys.maxint
        for i in lst1:
            idx = bisect_left(lst2, i)
            for nei in (-1, 0):
                if 0 <= idx+nei < len(lst2):
                    mini = min(mini, abs(i-lst2[idx+nei]))

        return mini