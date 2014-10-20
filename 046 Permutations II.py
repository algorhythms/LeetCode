"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
__author__ = 'Danyang'
class Solution:
    def permuteUnique_TLE(self, num):
        """
        list to set
        Time Limit Exceeded
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result = []
        self.get_permute(num, [], result)
        return map(list, set(map(tuple, result)))


    def get_permute_TLE(self, nums, current, result):
        length = len(nums)
        if length==0:
            result.append(current)

        for ind, val in enumerate(nums):
            self.get_permute(nums[:ind]+nums[ind+1:], current+[val], result)


    def permuteUnique(self, num):
        """
        Jump
        compared to 045 Permutation, two lines added: sort and continue
        :param num: a list of integer
        :return: a list of lists of integers
        """
        result = []
        num.sort()
        self.get_permute(num, [], result)
        return result

    def get_permute(self, nums, current, result):
        if not nums:
            result.append(current)

        for ind, val in enumerate(nums):
            if ind-1>=0 and val==nums[ind-1]: continue  # JUMP; only need to compare to previous value
            self.get_permute(nums[:ind]+nums[ind+1:], current+[val], result)

if __name__=="__main__":
    print Solution().permuteUnique([1, 1, 2])