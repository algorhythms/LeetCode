"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an
algorithm to find the maximum profit.
"""
__author__ = 'Danyang'


class Solution(object):
    def maxProfit(self, A):
        """
        Maximum subarray sum
        DP version
        Let F[i] be the maximum subarray sum ending at A[i-1]
        """
        if len(A) <= 1:
            return 0

        n = len(A)
        F = [0 for _ in xrange(n+1)]
        maxa = 0
        for i in xrange(2, n+1):
            F[i] = max(F[i-1] + A[i-1] - A[i-2], 0)  # revert the previous transaction
            maxa = max(maxa, F[i])

        return maxa

    def maxProfitDelta(self, prices):
        """
        Only long position allowed, cannot short

        Algorithm: max-array problem

        convert to maximum sub-array problem
        two pointer

        :param prices: a list of integer
        :return: integer, max profit
        """
        if len(prices) <= 1:
            return 0
        delta_prices = []
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        # O(n)
        # notice: possible to do nothing thus profit at least is 0 
        max_sub_array = 0
        current_sub_array = 0
        for j in xrange(len(delta_prices)):
            current_sub_array = max(0, current_sub_array+delta_prices[j])
            max_sub_array = max(max_sub_array, current_sub_array)

        return max_sub_array


if __name__ == "__main__":
    assert Solution().maxProfit([3, 2, 1, 4, 5, 6, 2]) == 5