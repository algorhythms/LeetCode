"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""
__author__ = 'Daniel'


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        sb = []  # string builder
        while n:
            n -= 1  # there is not 0 representation in excel title
            sb.append(chr(ord("A")+n%26))
            n /= 26

        return "".join(reversed(sb))

