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
        path_set = set()
        if not self.dfs(V, edges[0][0], None, visited, path_set):
            return False

        return len(visited) == n

    def dfs(self, V, k, pi, visited, path_set):
        if k in path_set:
            return False

        path_set.add(k)
        for neighbor in V[k]:
            if neighbor != pi:
                if not self.dfs(V, neighbor, k, visited, path_set):
                    return False

        path_set.remove(k)
        visited.add(k)
        return True