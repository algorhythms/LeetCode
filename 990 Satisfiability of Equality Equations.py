#!/usr/bin/python3
"""
Given an array equations of strings that represent relationships between
variables, each string equations[i] has length 4 and takes one of two different
forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily
different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names
so as to satisfy all the given equations.



Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is
satisfied, but not the second.  There is no way to assign the variables to
satisfy both equations.
Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
Example 3:

Input: ["a==b","b==c","a==c"]
Output: true
Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false
Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true

Note:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] and equations[i][3] are lowercase letters
equations[i][1] is either '=' or '!'
equations[i][2] is '='
"""
from typing import List


class DisjointSet:
    def __init__(self):
        self.pi = {}

    def union(self, x, y):
        self.pi[self.find(x)] = self.find(y)

    def find(self, x):
        if x not in self.pi:
            self.pi[x] = x
        elif self.pi[x] != x:
            self.pi[x] = self.find(self.pi[x])
        return self.pi[x]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """
        union find
        """
        ds = DisjointSet()
        neqs = []  # list of neq
        for e in equations:
            a = e[0]
            b = e[-1]
            sign = e[1:-1]
            if sign == "==":
                ds.union(a, b)
            else:
                neqs.append((a, b))

        for a, b in neqs:
            if ds.find(a) == ds.find(b):
                return False

        return True
