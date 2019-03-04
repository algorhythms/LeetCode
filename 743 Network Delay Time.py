#!/usr/bin/python3
"""
There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w),
where u is the source node, v is the target node, and w is the time it takes for
a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes
to receive the signal? If it is impossible, return -1.

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Dijkstra's algorithm
        """
        G = defaultdict(dict)
        reach_time = [float('inf') for _ in range(N + 1)]
        for u, v, w in times:
            G[u][v] = w

        h = [(0, K)]
        reach_time[K] = 0
        while h:
            t, s = heapq.heappop(h)
            if s in G:
                for d, w in G[s].items():
                    if t + w < reach_time[d]:
                        reach_time[d] = t + w
                        heapq.heappush(h, (t + w, d))

        ret = max(reach_time[1:])  # notice reach_time[0] is dummy
        if ret == float('inf'):
            return -1
        return ret


if __name__ == "__main__":
    assert Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
