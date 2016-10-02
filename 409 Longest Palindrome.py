"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be
built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = defaultdict(int)
        for elt in s:
            c[elt] += 1

        ret = 0
        for v in c.values():
            ret += (v/2) * 2

        if any(map(lambda x: x % 2 == 1, c.values())):
            ret += 1

        return ret


if __name__ == "__main__":
    assert Solution().longestPalindrome("abccccdd") == 7
