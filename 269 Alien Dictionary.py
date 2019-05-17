#!/usr/bin/python3
"""
There is a new alien language which uses the latin alphabet. However, the order
among letters are unknown to you. You receive a list of non-empty words from the
dictionary, where words are sorted lexicographically by the rules of this new
language. Derive the order of letters in this language.

Example 1:

Input:
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

Output: "wertf"
Example 2:

Input:
[
  "z",
  "x"
]

Output: "zx"
Example 3:

Input:
[
  "z",
  "x",
  "z"
]

Output: ""

Explanation: The order is invalid, so return "".
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        V = self.construct_graph(words)
        visited = set()
        pathset = set()
        ret = []
        for v in V.keys():
            if v not in visited:
                if not self.topo_dfs(V, v, visited, pathset, ret):
                    return ""

        return "".join(reversed(ret))

    def construct_graph(self, words):
        V = defaultdict(list)
        # need to initialize, consider test case ["z", "z"]
        for w in words:  # pitfall
            for c in w:
                V[c]
        for i in xrange(len(words) - 1):  # compare word_i and word_{i+1}
            for j in xrange(min(len(words[i]), len(words[i+1]))):
                if words[i][j] != words[i+1][j]:
                    V[words[i][j]].append(words[i+1][j])
                    break  # need to break for lexical order

        return V

    def topo_dfs(self, V, v, visited, pathset, ret):
        """
        Topological sort
        :param V: Vertices HashMap
        :param v: currently visiting letter
        :param visited: visited letters
        :param pathset: marked predecessor in the path
        :param ret: the path, ordered  topologically
        :return: whether contains cycles
        """
        if v in pathset:
            return False

        pathset.add(v)
        for nbr in V[v]:
            if nbr not in visited:
                if not self.topo_dfs(V, nbr, visited, pathset, ret):
                    return False

        pathset.remove(v)
        visited.add(v)  # add visited is in the end rather than at the begining
        ret.append(v)  # append after lower values
        return True

    def construct_graph_tedious(self, words, up, down, ptr, V):
        """
        :param words:
        :param up: upper bound
        :param down: lower bound + 1
        :param ptr: starting index for the char in the word
        :param V: Vertices
        :return: None
        """
        i = up
        while i < down:
            if ptr >= len(words[i]):
                i += 1
            else:
                if words[i][ptr] not in V:
                    V[words[i][ptr]] = []

                j = i+1
                while j < down and ptr < len(words[j]) and words[j][ptr] == words[i][ptr]:
                    j += 1

                self.construct_graph_tedious(words, i, j, ptr+1, V)
                if j < down and ptr < len(words[j]):
                    V[words[i][ptr]].append(words[j][ptr])

                i = j


if __name__ == "__main__":
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    assert Solution().alienOrder(lst) == "zyxwvutsrqponmlkjihgfedcba"
