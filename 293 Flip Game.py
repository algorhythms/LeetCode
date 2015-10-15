"""
Premium Question
Straightforward
"""
__author__ = 'Daniel'


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        for i in xrange(len(s)-1):
            if s[i:i+2] == "++":
                ret.append(s[:i]+"--"+s[i+2:])

        return ret