#!/usr/bin/python3
"""
Given two words word1 and word2, find the minimum number of steps required to
make word1 and word2 the same, where in each step you can delete one character
in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
"""
from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Longest Common Subsequence (LCS)
        Find the LCS, and delete the char in BOTH strings into LCS

        Let F[i][j] be length of LCS word1[:i] and word2[:j]

        F[i][j] = F[i-1][j-1] + 1 if word1[i-1] == word2[j-1]
        F[i][j] = max(F[i-1][j], F[i][j-1])
        """
        F = defaultdict(lambda: defaultdict(int))
        m = len(word1)
        n = len(word2)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    F[i][j] = F[i-1][j-1] + 1
                else:
                    F[i][j] = max(
                        F[i-1][j],
                        F[i][j-1],
                    )

        return m - F[m][n] + n - F[m][n]

    def minDistance_edit_distance(self, word1: str, word2: str) -> int:
        """
        Edit distance

        Let F[i][j] be # operations to make same for word1[:i] and word2[:j]

        F[i][j] = F[i-1][j-1] if word1[i-1] == word2[j-1]
        F[i][j] = min(F[i-1][j] + 1, F[i][j-1] + 1)
        """
        F = defaultdict(lambda: defaultdict(int))
        m = len(word1)
        n = len(word2)

        # initialization is important
        for i in range(1, m + 1):
            F[i][0] = i
        for j in range(1, n + 1):
            F[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    F[i][j] = F[i-1][j-1]
                else:
                    F[i][j] = min(
                        F[i-1][j] + 1,
                        F[i][j-1] + 1,
                    )

        return F[m][n]


if __name__ == "__main__":
    assert Solution().minDistance("sea", "eat") == 2
