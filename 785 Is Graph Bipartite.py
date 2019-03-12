#!/usr/bin/python3
"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two
independent subsets A and B such that every edge in the graph has one node in A
and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for
which the edge between nodes i and j exists.  Each node is an integer between 0
and graph.length - 1.  There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.


Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in
graph[j].
"""
from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        coloring the graph
        dfs coloring
        """
        G = graph
        color = defaultdict(int)
        for k in range(len(G)):
            if k not in color:
                color[k] = 0
                if not self.dfs(G, k, color):
                    return False
            # if colored, don't vist

        return True

    def dfs(self, G, u, color):
        for nbr in G[u]:
            if nbr in color:
                if color[nbr] == color[u]:
                    return False
            else:
                color[nbr] = 1 - color[u]  # can be (0, 1) or (-1, 1)
                if not self.dfs(G, nbr, color):
                    return False

        return True


class SolutionError:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        G = graph
        A, B = set(), set()
        visited = defaultdict(bool)
        for k in range(len(G)):
            if not visited[k]:
                if not self.dfs(G, visited, k, A, B, True):
                    return False

        return True

    def dfs(self, G, visited, u, A, B, is_A):
        visited[u] = True
        if is_A:
            A.add(u)
        else:
            B.add(u)

        for nbr in G[u]:
            if nbr in A if is_A else B:
                return False
            if not visited[nbr]:
                if not self.dfs(G, visited, nbr, A, B, False):
                    return False

        return True
