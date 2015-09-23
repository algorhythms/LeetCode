"""
Premium question
"""
__author__ = 'Daniel'


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        String

        :type s: str
        :type t: str
        :rtype: bool
        """
        l_s = len(s)
        l_t = len(t)
        if abs(l_s-l_t) > 1:
            return False

        if l_s > l_t:
            s, t = t, s
            l_s, l_t = l_t, l_s

        error = 0
        i, j = 0, 0
        while i < l_s and j < l_t:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if l_s != l_t:
                    j += 1
                else:
                    i += 1
                    j += 1

                error += 1

        return error == 1 or error == 0 and l_s != l_t
