"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbrev = defaultdict(int)
        self.dictionary = set(dictionary)

        for word in dictionary:
            self.abbrev[self.process(word)] += 1

    def process(self, word):
        if len(word) <= 2:
            return word

        return word[0]+str(len(word)-2)+word[-1]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        return (word in self.dictionary and self.abbrev[self.process(word)] == 1 or
                not self.process(word) in self.abbrev)
