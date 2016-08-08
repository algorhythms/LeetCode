"""
Write a function that takes a string as input and reverse only the vowels of a string.
"""
__author__ = 'Daniel'


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        j = len(s) - 1
        i = 0
        while i < j:
            if s[i] in vowels:
                while s[j] not in vowels: j -= 1
                s[i], s[j] = s[j], s[i]
                j -= 1

            i += 1

        return "".join(s)