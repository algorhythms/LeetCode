"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""
__author__ = 'Daniel'


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sig = 1
        ret = 0
        for i in xrange(len(s)-1, -1, -1):
            ret += sig*(ord(s[i])-ord('A')+1)
            sig *= 26

        return ret