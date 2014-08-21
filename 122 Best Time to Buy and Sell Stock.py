__author__ = 'Danyang'
class Solution:
    def maxProfit(self, prices):
        """
        Only long position allowed, cannot short

        convert to maximum sub-array problem
        two pointer
        :param prices: a list of integer
        :return: integer, max profit
        """
        if len(prices)<=1:
            return 0
        delta_prices = []
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        # two pointers O(n)

        max_sub_array = 0
        current_sub_array = 0
        for j in xrange(len(delta_prices)):
            if current_sub_array+delta_prices[j]>=0:
                current_sub_array += delta_prices[j]
            else:
                current_sub_array = 0
            max_sub_array = max(max_sub_array, current_sub_array)


        return max_sub_array

if __name__=="__main__":
    print Solution().maxProfit([3, 2, 1, 4, 5, 6, 2])