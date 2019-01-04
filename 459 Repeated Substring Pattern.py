#!/usr/bin/python3
"""
Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together. You may assume
the given string consists of lowercase English letters only and its length will
not exceed 10000.
"""


class Solution:
    def repeatedSubstringPattern(self, s):
        """
        The start of the substring is always 0, then incr the ending index e
        until n/2 where n = len(s)
        Brute force: O(n/2) * O(n)

        test substring using KMP is O(|target|)

        if s is composed of n substrings p, then s2 = s + s should contain
        2n * p.

        Destroying the first and the last character leads to at
        least (2n - 2) * p left.

        n >= 2
        2n - 2 >= n
        S1[1:-1] should still contain S
        :type s: str
        :rtype: bool
        """
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern_error(self, s):
        """
        Two pointers algorithm. The start of the substring is always 0
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        p1 = 0
        e = 1  # ending s[0:e] is the substring
        p2 = 1
        while p2 < len(s):
            if s[p1] == s[p2]:
                p1 += 1
                if p1 == e:
                    p1 = 0
            else:
                p1 = 0
                e = p2 + 1

            p2 += 1

        return p2 == len(s) and p1 == 0 and e != len(s)


if __name__ == "__main__":
    assert Solution().repeatedSubstringPattern("abab") == True
    assert Solution().repeatedSubstringPattern("abcd") == False
    assert Solution().repeatedSubstringPattern("abacababacab") == True
