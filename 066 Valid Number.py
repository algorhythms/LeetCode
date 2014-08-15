__author__ = 'Danyang'
class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False