"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
__author__ = 'Daniel'


class Solution:
    def maxProfit(self, k, prices):
        """
        DP
        local_{i,j} = \max(global_{i-1.j-1}+\Delta, local_{i-1,j}+\Delta)

        global_{i,j} = \max(local_{i, j}, global_{i-1,j})
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n:
            return self.maxProfit_unlimited_transactions(prices)

        l = [0 for _ in xrange(k+1)]  # local max
        g = [0 for _ in xrange(k+1)]  # global max
        gmax = 0
        for i in xrange(1, n):
            diff = prices[i] - prices[i-1]
            for j in xrange(k, 0, -1):
                l[j] = max(g[j-1]+diff, l[j]+diff)
                g[j] = max(l[j], g[j])
                gmax = max(gmax, g[j])

        return gmax

    def maxProfit_unlimited_transactions(self, prices):
        profit = 0
        for i in xrange(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit

if __name__ == "__main__":
    print Solution().maxProfit(2, [1, 2, 4])