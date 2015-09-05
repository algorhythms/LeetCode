"""
Premium Question
"""
import sys
from bisect import bisect_left

__author__ = 'Daniel'


class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: list[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos_lst1 = [pos for pos, v in enumerate(words) if v == word1]
        pos_lst2 = [pos for pos, v in enumerate(words) if v == word2]
        mini = sys.maxint
        for pos in pos_lst1:
            idx = bisect_left(pos_lst2, pos)
            for nei in (-1, 0):
                if 0 <= idx+nei < len(pos_lst2) and pos != pos_lst2[idx+nei]:
                    mini = min(mini, abs(pos-pos_lst2[idx+nei]))

        return mini
