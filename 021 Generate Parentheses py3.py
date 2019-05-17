#!/usr/bin/python3
"""
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Method 1 - backtracking
        Method 2 - dp
        Let F[n] be the list of parentheses at length 2n
        """
        F: List[List[str]] = [[] for _ in range(n + 1)]
        F[0].append("")
        for i in range(1, n+1):
            for j in range(i):
                for s1 in F[j]:
                    for s2 in F[i-j-1]:
                        F[i].append(f"({s1}){s2}")

        return F[n]
