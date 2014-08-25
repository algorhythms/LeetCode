__author__ = 'Danyang'
class Solution:
    def combine(self, n, k):
        """
        Similar to 045 Permutation

        :param n: int
        :param k: int
        :return: a list of lists of integers
        """
        result = []
        nums = [i+1 for i in xrange(n)]  # sorted, avoid duplicate
        self.get_combination(k, nums, [], result)
        return result

    def get_combination(self, k, nums, current, result):
        if len(current)==k:
            result.append(current)
            return  # prune
        elif len(current)+len(nums)<k:
            return  # prune

        for ind, val in enumerate(nums):
            # try:
            self.get_combination(k, nums[ind+1:], current+[val], result)  # list(current).append(val) is side-effect
            # except IndexError:
            #     self.get_combination(k, [], current+[val], result)
            # array slice out of index will return []


if __name__=="__main__":
    print Solution().combine(4, 2)