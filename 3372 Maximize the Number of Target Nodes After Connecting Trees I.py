#!/usr/bin/python3
"""
There exist two undirected trees with n and m nodes, with distinct labels in ranges [0, n - 1] and [0, m - 1], respectively.

You are given two 2D integer arrays edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the first tree and edges2[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the second tree. You are also given an integer k.

Node u is target to node v if the number of edges on the path from u to v is less than or equal to k. Note that a node is always target to itself.

Return an array of n integers answer, where answer[i] is the maximum possible number of nodes target to node i of the first tree if you have to connect one node from the first tree to another node in the second tree.

Note that queries are independent from each other. That is, for every query you will remove the added edge before proceeding to the next query.

Example 1:

Input: edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], k = 2

Output: [9,7,9,8,8]

Explanation:

For i = 0, connect node 0 from the first tree to node 0 from the second tree.
For i = 1, connect node 1 from the first tree to node 0 from the second tree.
For i = 2, connect node 2 from the first tree to node 4 from the second tree.
For i = 3, connect node 3 from the first tree to node 4 from the second tree.
For i = 4, connect node 4 from the first tree to node 4 from the second tree.

Example 2:

Input: edges1 = [[0,1],[0,2],[0,3],[0,4]], edges2 = [[0,1],[1,2],[2,3]], k = 1

Output: [6,3,3,3,3]

Explanation:

For every i, connect node i of the first tree with any node of the second tree.

Constraints:

2 <= n, m <= 1000
edges1.length == n - 1
edges2.length == m - 1
edges1[i].length == edges2[i].length == 2
edges1[i] = [ai, bi]
0 <= ai, bi < n
edges2[i] = [ui, vi]
0 <= ui, vi < m
The input is generated such that edges1 and edges2 represent valid trees.
0 <= k <= 1000
"""
from collections import defaultdict


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        Just greedily connect to the highest cardinality.
        2nd tree only calculate k-1
        """
        n = len(edges1) + 1
        m = len(edges2) + 1
        G1 = defaultdict(list)
        for u, v in edges1:
            G1[u].append(v)
            G1[v].append(u)

        cardinality1 = [self.getCardinality(G1, i, k, [False] * n) for i in range(n)]

        G2 = defaultdict(list)
        for u, v in edges2:
            G2[u].append(v)
            G2[v].append(u)

        cardinality2 = [self.getCardinality(G2, i, k - 1, [False] * m) for i in range(m)]
        max2 = max(cardinality2)
        return [
            cardinality1[i] + max2
            for i in range(n)
        ]

    def getCardinality(self, G, u, k, visited):
        # dfs
        cardinality = 1
        visited[u] = True
        for nbr in G[u]:
            if not visited[nbr] and k - 1 >= 0:
                cardinality += self.getCardinality(G, nbr, k - 1, visited)
        
        return cardinality