"""
Premium Question
"""
from bisect import bisect_left
from collections import defaultdict
import sys

__author__ = 'Daniel'


class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.

        :type words: list[str]
        """
        self.word_dict = defaultdict(list)
        for i, w in enumerate(words):
            self.word_dict[w].append(i)


    def shortest(self, word1, word2):
        """

        :type word1: str
        :type word2: str
        :rtype: int
        """
        mini = sys.maxint
        for i in self.word_dict[word1]:
            idx = bisect_left(self.word_dict[word2], i)
            for nei in (-1, 0):
                if 0 <= idx+nei < len(self.word_dict[word2]):
                    mini = min(mini, abs(i-self.word_dict[word2][idx+nei]))

        return mini
