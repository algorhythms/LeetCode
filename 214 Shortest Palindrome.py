"""
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the
shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
__author__ = 'Daniel'


class Solution:
    def shortestPalindrome(self, s):
        """
        KMP

        :type s: str
        :rtype: str
        """
        s_r = s[::-1]
        l = len(s)
        if l < 2:
            return s

        # construct T
        T = [0 for _ in xrange(l+1)]
        T[0] = -1
        pos = 2
        cnd = 0
        while pos <= l:
            if s[pos-1] == s[cnd]:
                T[pos] = cnd+1
                cnd += 1
                pos += 1
            elif T[cnd] != -1:
                cnd = T[cnd]
            else:
                T[pos] = 0
                cnd = 0
                pos += 1

        # search 
        i = 0
        b = 0
        while i+b < l:
            if s[i] == s_r[i+b]:
                i += 1
                if i == l:
                    return s
            elif T[i] != -1:
                b = b+i-T[i]
                i = T[i]
            else:
                b += 1
                i = 0

        # where it falls off
        return s_r+s[i:]


if __name__ == "__main__":
    assert Solution().shortestPalindrome("abcd") == "dcbabcd"


