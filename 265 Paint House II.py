"""
Premium Question
"""
import sys

__author__ = 'Daniel'


class Solution(object):
    def minCostII(self, costs):
        """
        Lef F[i][j] be the total min costs when the houses BEFORE i are painted, with (i-1)-th house pained as color j
        F[i][j] = \min(F[i-1][k] + cost[i-1][j] \forall k, k != j

        edge case handling for i
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)
        m = len(costs[0])
        F = [[0 for _ in xrange(m)] for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            for k1 in xrange(m):
                F[i][k1] = min(
                    F[i-1][k0]+costs[i-1][k1]
                    # if i == 1 or k1 != k0 else sys.maxint  # another syntax 
                    for k0 in xrange(m)
                    if i == 1 or k1 != k0
                )

        return min(F[n][i] for i in xrange(m))


if __name__ == "__main__":
    assert Solution().minCostII([[8]]) == 8