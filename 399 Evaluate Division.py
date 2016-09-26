"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number
(floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
where equations.size() == values.size(), and the values are positive. This represents the equations. Return
vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

"""
from collections import defaultdict
from itertools import izip

__author__ = 'Daniel'


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        transitive closure
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(dict)
        for edge, val in izip(equations, values):
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        return [self.dfs(G, s, e, set()) for s, e in queries]

    def dfs(self, G, s, e, path):
        if s not in G or e not in G:
            return -1.0
        if e in G[s]:
            return G[s][e]
        for nbr in G[s]:
            if nbr not in path:
                path.add(nbr)
                val = self.dfs(G, nbr, e, path)
                if val != -1.0:
                    return val * G[s][nbr]
                path.remove(nbr)

        return -1.0


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        Floyd-Warshall algorithm
        transitive closure
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(dict)
        for edge, val in izip(equations, values):
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        # Floyd-Warshall
        for mid in G:
            for s in G[mid]:
                for e in G[mid]:
                    G[s][e] = G[s][mid] * G[mid][e]

        return [G[s].get(e, -1.0) for s, e in queries]

