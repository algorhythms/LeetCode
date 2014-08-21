__author__ = 'Danyang'
class Solution:
    def maxProfit_error(self, prices):
        """
        2 transactions
        you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

        :param prices: list of integers
        :return: integer
        """

        if len(prices)<=1:
            return 0

        delta_prices = []
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        # O(n)
        max_profits = [0, 0]

        max_sub_array = 0
        current_sub_array = 0
        for j in xrange(len(delta_prices)):
            if current_sub_array+delta_prices[j]>=0:
                current_sub_array += delta_prices[j]
                max_sub_array = max(max_sub_array, current_sub_array)
            else:
                # keep two 2
                self.keep_top_2(max_profits, max_sub_array)
                max_sub_array = 0
                current_sub_array = 0

        return sum(max_profits)

    def keep_top_2(self, max_profits, candidate):
        if candidate>max_profits[0]:
            max_profits[1] = max_profits[0]
            max_profits[0] = candidate
        elif candidate>max_profits[1]:
            max_profits[1] = candidate


    def maxProfit(self, prices):
        """
        2 transactions
        you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

        http://www.darrensunny.me/leetcode-best-time-to-buy-and-sell-stock-iii/
        :param prices: list of integers
        :return: integer
        """
        if len(prices)<=1:
            return 0

        # O(n) using dp
        forward = [0 for _ in xrange(len(prices))]  # forward 0..i
        lowest_buy_price = prices[0]
        for i in xrange(0, len(prices)):
            if i==0:
                forward[i] = 0
            else:
                forward[i] = max(forward[i-1], prices[i]-lowest_buy_price)

            lowest_buy_price = min(prices[i], lowest_buy_price)

        backward = [0 for _ in xrange(len(prices))]  # backward i..len-1
        highest_sell_price = prices[-1]
        for i in xrange(len(prices)-1, -1, -1):
            if i==len(prices)-1:
                backward[i] = 0
            else:
                backward[i] = max(backward[i+1], highest_sell_price-prices[i])

            highest_sell_price = max(prices[i], highest_sell_price)

        max_profit = 0
        for i in xrange(len(prices)):
            max_profit = max(max_profit, forward[i]+backward[i])
        return max_profit