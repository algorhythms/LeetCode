#!/usr/bin/python3
"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
repeats forever. For example if routes[0] = [1, 5, 7], this means that the first
bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop
T. Travelling by buses only, what is the least number of buses we must take to
reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second
bus to the bus stop 6.

Note:
1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
"""
from typing import List
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        BFS
        bus based nodes rather than stop based nodes

        BFS = O(|V| + |E|) = O(N + N^2), where N is number of routes
        Construction = O (N^2 * S), where S is number of stops
        """
        if S == T:
            return 0

        routes = [set(e) for e in routes]
        G = defaultdict(set)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                stops_1, stops_2 = routes[i], routes[j]  # bus represented by stops
                for stop in stops_1:  # any(stop in stops_2 for stop in stops_1)
                    if stop in stops_2:
                        G[i].add(j)
                        G[j].add(i)
                        break

        q = [i for i, stops in enumerate(routes) if S in stops]
        target_set = set([i for i, stops in enumerate(routes) if T in stops])
        visited = defaultdict(bool)
        for i in q:
            visited[i] = True
        step = 1
        while q:
            cur_q = []
            for e in q:
                if e in target_set:
                    return step
                for nbr in G[e]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        cur_q.append(nbr)

            step += 1
            q = cur_q

        return -1

    def numBusesToDestination_TLE(self, routes: List[List[int]], S: int, T: int) -> int:
        """
        BFS
        Lest number of buses rather than bus stops

        Connect stops within in bus use one edge in G
        """
        G = defaultdict(set)
        for stops in routes:
            for i in range(len(stops)):
                for j in range(i + 1, len(stops)):
                    u, v = stops[i], stops[j]
                    G[u].add(v)
                    G[v].add(u)

        q = [S]
        step = 0
        visited = defaultdict(bool)
        visited[S] = True  # avoid add duplicate
        while q:
            cur_q = []
            for e in q:
                if e == T:
                    return step
                for nbr in G[e]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        cur_q.append(nbr)

            step += 1
            q = cur_q

        return -1


if __name__ == "__main__":
    assert Solution().numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6) == 2
