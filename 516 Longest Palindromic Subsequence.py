#!/usr/bin/python3
"""
Given a string s, find the longest palindromic subsequence's length in s. You
may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""
from collections import defaultdict


class Solution:
    def longestPalindromeSubseq(self, s):
        """
        Brute force 0-1, exponential

        F[i][j] be the longest palindrom subseuence (not necessarily ending at
        A[i] A[j])

        F[i-1]F[j+1] = F[i][j] + 2 or F[i][j]  # error
        The transition function shoud be
        F[i][j] = F[i+1][j-1] + 2 or F[i+1][j] or F[i][j-1]
        :type s: str
        :rtype: int
        """
        n = len(s)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            F[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                F[i][j] = max(F[i+1][j], F[i][j-1])
                if s[i] == s[j]:
                    F[i][j] = max(F[i][j], F[i+1][j-1] + 2)

        return F[0][n-1]


if __name__ == "__main__":
    assert Solution().longestPalindromeSubseq("bbbab") == 4
