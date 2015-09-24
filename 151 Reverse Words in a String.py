"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
"""
__author__ = 'Danyang'


class Solution:
    def reverseWords(self, s):
        """
        Notice: ask how to deal with punctuations
        :param s: a string
        :return: a string
        """
        words_lst = s.split()  # not s.split(" ")
        words_lst = reversed(words_lst)
        return ' '.join(words_lst)