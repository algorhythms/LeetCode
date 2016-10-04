"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the
itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read
as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
import heapq
from collections import defaultdict, deque

__author__ = 'Daniel'


class Solution(object):
    def findItinerary(self, tickets):
        """
        Euler path
        Hierholzer's algorithm a Euler path, must be directed graph
        The graph must be directed graph
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        G = defaultdict(list)
        for elt in tickets:
            s, e = elt
            heapq.heappush(G[s], e)  # heap lexical order

        ret = deque()
        self.dfs(G, 'JFK', ret)
        return list(ret)

    def dfs(self, G, cur, ret):
        while G[cur]:
            self.dfs(G, heapq.heappop(G[cur]), ret)

        ret.appendleft(cur)


if __name__ == "__main__":
    assert Solution().findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]) == ['JFK', 'NRT', 'JFK', 'KUL']
