"""
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted
tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a
graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected
edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1,
0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        Longest path algorithm
        Diameter of a tree
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return [0]

        V = {i: [] for i in xrange(n)}
        for a, b in edges:
            V[a].append(b)
            V[b].append(a)

        # longest path algorithm
        _, _, last = self.bfs(0, V)
        level, pi, last = self.bfs(last, V)

        ret = []
        cur = last
        for _ in xrange((level-1)/2):
            cur = pi[cur]
        ret.append(cur)

        if level%2 == 0:
            ret.append(pi[cur])

        return ret

    def bfs(self, s, V):
        # bfs
        visited = [False for _ in xrange(len(V))]
        pi = [-1 for _ in xrange(len(V))]
        last = s
        level = 0
        q = []
        q.append(s)
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                last = cur
                visited[cur] = True
                for nbr in V[cur]:
                    if not visited[nbr]:
                        pi[nbr] = cur
                        q.append(nbr)

            q = q[l:]
            level += 1

        return level, pi, last


class Solution_TLE(object):
    def findMinHeightTrees_TLE(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return 0

        V = {i: [] for i in xrange(n)}
        for a, b in edges:
            V[a].append(b)
            V[b].append(a)

        ret = []
        mini = n
        for k in V.keys():
            l = self.bfs(k, V)
            if l < mini:
                ret = [k]
                mini = l
            elif l == mini:
                ret.append(k)

        return ret

    def bfs(self, s, V):
        # bfs
        visisted = [False for _ in xrange(len(V))]
        q = []
        level = 0
        q.append(s)
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                visisted[cur] = True
                for nbr in V[cur]:
                    if not visisted[nbr]:
                        q.append(nbr)

            q = q[l:]
            level += 1

        return level


class SolutionError(object):
    def findMinHeightTrees(self, n, edges):
        """
        One pass
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return 0

        V = {i: [] for i in xrange(n)}
        for a, b in edges:
            V[a].append(b)
            V[b].append(a)

        leaf = None
        for k, v in V.items():
            if len(v) == 1:
                leaf = k
                break

        # bfs
        visisted = [False for _ in xrange(n)]
        h2v = defaultdict(list)
        q = []
        level = 0
        q.append(leaf)
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                h2v[level].append(cur)
                visisted[cur] = True
                for nbr in V[cur]:
                    if not visisted[nbr]:
                        q.append(nbr)

            q = q[l:]
            level += 1

        if level%2 == 0:
            return h2v[level/2-1]+h2v[level/2]
        else:
            return h2v[level/2]


if __name__ == "__main__":
    # print Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
    assert Solution().findMinHeightTrees(7, [[0, 1], [1, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [1, 2]