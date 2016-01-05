"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
__author__ = 'Danyang'


class Solution(object):
    def numDecodings(self, s):
        """
        F
        Let F[i] be the number of decode ways for s[:i]
        - 1 2 2 3 1 2 2 3
        1 1 2 ? ?
        F[i] = (F[i-1]) + optional(F[i-2]))

        notice the special handling for "0

        :param s: a string
        :return: an integer
        """
        if s.startswith("0"):
            return 0

        n = len(s)
        if not s:
            return 0
        F = [0 for _ in xrange(n+1)]
        F[0] = 1
        F[1] = 1

        for i in xrange(2, n+1):
            if s[i-1] != "0":
                F[i] = F[i-1]
                if 10 <= int(s[i-2]+s[i-1]) < 27:
                    F[i] += F[i-2]
            else:  # 0 is special
                if s[i-2] in ("1", "2"):
                    F[i] = F[i-2]
                else:
                    return 0

        return F[-1]


if __name__ == "__main__":
    assert Solution().numDecodings("10") == 1
    assert Solution().numDecodings("27") == 1
    assert Solution().numDecodings("12") == 2
    assert Solution().numDecodings("0") == 0