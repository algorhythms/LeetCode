"""
Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
"""
__author__ = 'Danyang'
class Solution:
    def strStr(self, haystack, needle):
        """
        Algorithm:
        two pointers

        KMP algorithm # TODO
        :param haystack: str
        :param needle: str
        :return: str or None
        """
        l_hay = len(haystack)
        l_ndl = len(needle)
        for i in xrange(l_hay-l_ndl+1):  # i+l_ndl <= l_hay
            if haystack[i:i+l_ndl]==needle:
                return haystack[i:]
        return None
