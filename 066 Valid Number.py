"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before
implementing one.
"""
__author__ = 'Danyang'
class Solution:
    def isNumber(self, s):
        """
        using built-in function
        :param s: a string
        :return: boolean
        """
        try:
            float(s)
            return True
        except ValueError:
            return False