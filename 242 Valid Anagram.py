"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution:
    def isAnagram(self, s, t):
        """
        bucket

        :type s: str
        :type t: str
        :rtype: bool
        """
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1

        for c in t:
            if c not in cnt or cnt[c] < 1:
                return False

            cnt[c] -= 1

        for v in cnt.values():
            if v != 0:
                return False

        return True
