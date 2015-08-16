"""
Premium Question
"""
import sys

__author__ = 'Daniel'


class Solution:
    # @param {integer[][]} costs
    # @return {integer}
    def minCost(self, costs):
        """
        Lef F[i][j] be the total min costs when the houses BEFORE i are painted, with (i-1)-th house pained as color j
        :type costs: list[list[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)
        m = len(costs[0])
        F = [[0 for _ in xrange(m)] for _ in xrange(n+1)]
        for k in xrange(1, n+1):
            for i in xrange(m):
                F[k][i] = sys.maxint
                for j in xrange(m):
                    if i != j:
                        F[k][i] = min(F[k][i], F[k-1][j]+costs[k-1][i])

        return min(F[n][i] for i in xrange(m))


if __name__ == "__main__":
    costs = [[7, 6, 2]]
    assert Solution().minCost(costs) == 2