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
from typing import List
from collections import defaultdict, deque


class Solution(object):
    def alienOrder(self, words: List[str]) -> str:
        G = self.construct_graph(words)
        visited = defaultdict(int)  # 0 not visited, 1 visiting, 2 visted
        ret = deque()
        for u in G.keys():
            if visited[u] == 0:
                if not self.topo_dfs(G, u, visited, ret):
                    return ""

        return "".join(ret)

    def construct_graph(self, words):
        G = defaultdict(list)
        # need to initialize, consider test case ["z", "z"]
        for w in words:  # error
            for c in w:
                G[c]

        for i in range(len(words) - 1):  # compare word_i and word_{i+1}
            for c1, c2 in zip(words[i], words[i+1]):
                if c1 != c2:  # lexical order 
                    G[c1].append(c2)
                    break  # need to break for lexical order

        return G

    def topo_dfs(self, G, u, visited, ret):
        """
        Topological sort
        G = defaultdict(list)
        visited = defaultdict(int)  # 0 not visited, 1 visiteding, 2 visted

        pre-condition: u is not visited (0)
        """
        visited[u] = 1
        for nbr in G[u]:
            if visited[nbr] == 1:
                return False
            if visited[nbr] == 0:
                if not self.topo_dfs(G, nbr, visited, ret):
                    return False

        visited[u] = 2
        ret.appendleft(u)  # visit larger first
        return True


if __name__ == "__main__":
    lst = ["ze", "yf", "xd", "wd", "vd", "ua", "tt", "sz", "rd", "qd", "pz", "op", "nw", "mt", "ln", "ko", "jm", "il",
           "ho", "gk", "fa", "ed", "dg", "ct", "bb", "ba"]
    assert Solution().alienOrder(lst) == "zyxwvutsrqponmlkjihgfedcba"
