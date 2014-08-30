__author__ = 'Danyang'
class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        similar to maximum sub-array problem
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
        for ind, val in enumerate(diff):
            sum_before += val
            if sum_before<0:  # reset sum_before since gas insufficient for the journey
                start_index = ind+1
                sum_before = 0

        return start_index

if __name__=="__main__":
    Solution().canCompleteCircuit([5], [4])