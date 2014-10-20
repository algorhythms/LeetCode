"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word
in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""
__author__ = 'Danyang'
class Solution:
    def lengthOfLastWord(self, s):
        """
        String

        ... what is the meaning of this question?
        :param s: string
        :return: integer
        """
        s = s.strip()
        lst = s.split(" ")
        try:
            last_word = lst[-1]
            return len(last_word)
        except IndexError:
            return 0
