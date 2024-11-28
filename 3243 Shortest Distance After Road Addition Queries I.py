#!/usr/bin/python3
"""
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

queries[i] = [ui, vi] represents the addition of a new unidirectional road from city ui to city vi. After each query, you need to find the length of the shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1], answer[i] is the length of the shortest path from city 0 to city n - 1 after processing the first i + 1 queries.

 

Example 1:

Input: n = 5, queries = [[2,4],[0,2],[0,4]]

Output: [3,2,1]

Explanation:



After the addition of the road from 2 to 4, the length of the shortest path from 0 to 4 is 3.



After the addition of the road from 0 to 2, the length of the shortest path from 0 to 4 is 2.



After the addition of the road from 0 to 4, the length of the shortest path from 0 to 4 is 1.

Example 2:

Input: n = 4, queries = [[0,3],[0,2]]

Output: [1,1]

Explanation:



After the addition of the road from 0 to 3, the length of the shortest path from 0 to 3 is 1.



After the addition of the road from 0 to 2, the length of the shortest path remains 1.

 

Constraints:

3 <= n <= 500
1 <= queries.length <= 500
queries[i].length == 2
0 <= queries[i][0] < queries[i][1] < n
1 < queries[i][1] - queries[i][0]
There are no repeated roads among the queries.
"""
from collections import defaultdict, deque


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        G = defaultdict(list)
        dist = []
        for i in range(n-1):
            G[i].append(i+1)

        for i in range(n):
            dist.append(i)
        
        ret = []
        for u, v in queries:
            G[u].append(v)
            self.bfs(G, dist, u)
            ret.append(dist[~0])
        
        return ret
        
    def bfs(self, G, dist, s):
        """
        * Known origin and end destination
        * dist is the distance from origin, not to destination
        * BFS update the distance from the source, where the source is the 
        start of the new edge, not the origin of the graph
        """
        q = deque()
        q.append(s)
        while q:
            v = q.popleft()
            for nbr in G[v]:
                if dist[nbr] > dist[v] + 1:
                    # It and its descendants require distance update
                    dist[nbr] = dist[v] + 1
                    q.append(nbr)


class SolutionTLE:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Naive solution:
        1. maintain a graph 
        2. BFS
        """
        G = defaultdict(list)
        for i in range(n-1):
            G[i].append(i+1)
        
        ret = []
        for q in queries:
            s, t = q
            G[s].append(t)
            ret.append(self.bfs(G, 0, n - 1))

        return ret

    def bfs(self, G, s, t):
        q = [s]
        ret = 0
        while q:
            nxt_q = []
            ret += 1
            for v in q:
                for nbr in G[v]:
                    if nbr == t:
                        return ret 
                    nxt_q.append(nbr)

            q = nxt_q
