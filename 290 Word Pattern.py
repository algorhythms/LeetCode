"""
Given a pattern and a string str, find if str follows the same pattern.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
patterncontains only lowercase alphabetical letters, and str contains words separated by a single space. Each word in
str contains only lowercase alphabetical letters.
Both pattern and str do not have leading or trailing spaces.
Each letter in pattern must map to a word with length that is at least 1.
"""
__author__ = 'Daniel'


class Solution(object):
    def wordPattern(self, pattern, s):
        lst = s.split(" ")
        if len(pattern) != len(lst):
            return False

        char2word = {}
        words = set()
        for i in xrange(len(pattern)):
            if pattern[i] in char2word:
                if char2word[pattern[i]] != lst[i]:
                    return False
                else:
                    assert lst[i] in words
            else:
                if lst[i] in words:
                    return False
                char2word[pattern[i]] = lst[i]
                words.add(lst[i])

        return True


class OneToOneMap(object):
    def __init__(self):
        self.m = {}  # keep a single map

    def set(self, a, b):
        self.m[a] = b
        self.m[b] = a

    def get(self, a):
        return self.m.get(a)


class SolutionError(object):
    def wordPattern(self, pattern, str):
        """
        May not always work due to OneToOneMap implementation in the case that a word is 1-letter.

        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = OneToOneMap()
        lst = str.split(" ")
        if len(pattern) != len(lst):
            return False

        for i in xrange(len(pattern)):
            a = m.get(pattern[i])
            b = m.get(lst[i])
            if a is None and b is None:
                m.set(pattern[i], lst[i])
            elif a is None and b is not None:
                return False
            elif a != lst[i]:
                return False

        return True


if __name__ == "__main__":
    assert Solution().wordPattern("abba", "dog cat cat dog") == True
