"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell
one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you
must sell the stock before you buy again).
"""
__author__ = 'Danyang'


class Solution:
    def maxProfit(self, prices):
        """
        multiple transactions
        you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

        Algorithm: transformed array

        :param prices: list of integers
        :return: integer
        """
        if len(prices) <= 1:
            return 0

        delta_prices = []  # \delta
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        # O(n)
        profit = 0
        for i in xrange(len(delta_prices)):
            if delta_prices[i] > 0:
                profit += delta_prices[i]

        return profit