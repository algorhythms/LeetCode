"""
Premium Question
simple DFS
"""
__author__ = 'Daniel'


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        V = [[] for _ in xrange(n)]
        for e in edges:
            V[e[0]].append(e[1])
            V[e[1]].append(e[0])

        visited = [False for _ in xrange(n)]
        cnt = 0
        for v in xrange(n):
            if not visited[v]:
                cnt += 1
                self.dfs(V, v, visited)

        return cnt

    def dfs(self, V, v, visited):
        visited[v] = True
        for nbr in V[v]:
            if not visited[nbr]:
                self.dfs(V, nbr, visited)
