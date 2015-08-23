"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :edges: List[List[int]
        :rtype: bool
        """
        if not edges:
            return n in (0, 1)

        V = defaultdict(list)
        for edge in edges:
            V[edge[0]].append(edge[1])
            V[edge[1]].append(edge[0])

        visited = set()
        marked = set()
        if not self.dfs(V, edges[0][0], None, visited, marked):
            return False

        return len(visited) == n

    def dfs(self, V, k, pi, visited, marked):
        if k in marked:
            return False

        marked.add(k)
        for neighbor in V[k]:
            if neighbor != pi:
                if not self.dfs(V, neighbor, k, visited, marked):
                    return False

        marked.remove(k)
        visited.add(k)
        return True