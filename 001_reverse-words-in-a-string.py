__author__ = 'Danyang'
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words_lst = s.split() # not s.split(" ")
        words_lst = reversed(words_lst)
        return ' '.join(words_lst)