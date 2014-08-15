__author__ = 'Danyang'


class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        """
        String
        """
        s = s.strip()
        lst = s.split(" ")
        try:
            last_word = lst[-1]
            return len(last_word)
        except IndexError:
            return 0
