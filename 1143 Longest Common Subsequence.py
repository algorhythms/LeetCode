#!/usr/bin/python3
"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        """
        Let F_{i, j} be the longest common subsequence of a[:i] and b[:j]
        """
        m, n = len(a), len(b)
        F = [
            [0 for _ in range(n+1)]
            for _ in range(m+1)
        ]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if a[i-1] == b[j-1]:
                    F[i][j] = F[i-1][j-1] + 1
                else:
                    F[i][j] = max(F[i-1][j], F[i][j-1])
        
        return F[m][n]
