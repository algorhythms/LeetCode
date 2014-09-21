"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station
(i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
"""
__author__ = 'Danyang'
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """

              .-''''-.
              |==  ==|-.
              |~~ ~~~|`\\
              | FUEL | ||
              |      |//
              |      |/
              |      |
            __|______|__
           [____________]
        Algorithm:
        Similar to maximum sub-array problem

        1. determine whether can cover one cycle
        2. determine the start_index:
           define: sum[i, j] = sum(diff[k]) for i<=k<j

           start testing from i, sum[i, i+1]>0, iterate until reach j such that sum[i, j-1]>0, sum[i, j]<0, then do you
           need to go back to i+1? No, since sum[i, i+1]>0, you are better off starting from i with some gas left rather
           than i+1 with absolute 0 gas in the car. Do you need to go back to i+2? No, since sum[i, i+2]>0. Similarly,
           you do not need to start from i+3, i+4, ..., j. You only need to start the testing from j+1.

        :param gas: a list of integers
        :param cost: a list of integers, cost[i] from i to i+1
        :return: an integer
        """
        length = len(gas)

        # gas difference
        diff = [gas[i]-cost[i] for i in xrange(length)]

        # find whether can cover one cycle
        # starting from arbitrary point
        if sum(diff)<0:
            return -1

        # find the starting index
        start_index = 0
        sum_before = 0
        for ind, val in enumerate(diff):  # O(N), rather than brutal force O(N^2)
            sum_before += val
            if sum_before<0:  # reset sum_before since gas insufficient for the journey. # sum[i, j]<0
                start_index = ind+1
                sum_before = 0

        return start_index

if __name__=="__main__":
    Solution().canCompleteCircuit([5], [4])