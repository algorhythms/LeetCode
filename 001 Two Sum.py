"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be
less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
__author__ = 'Danyang'


class Solution:
    def twoSum_TLE(self, num, target):
        """
        built-in method .index
        :param num: list
        :param target: int
        :return: tuple, (index1, index2)
        """
        nums = num
        for ind1, val in enumerate(nums):
            try:
                ind2 = nums.index(target - val)
                return ind1+1, ind2+1
            except ValueError:
                continue

    def twoSum_TLE_2(self, num, target):
        nums = num
        for ind1, val in enumerate(nums):
            if target-val in nums:
                return ind1+1, nums.index(target-val)+1

    def twoSum(self, num, target):
        """
        Hash Map

        :param num: list
        :param target: int
        :return: tuple, (index1, index2)
        """
        hash_map = {}
        for ind, val in enumerate(num):
            hash_map[val] = ind

        for ind1, val in enumerate(num):
            if target-val in hash_map:
                ind2 = hash_map[target-val]
                if ind1!=ind2:
                    return ind1+1, ind2+1


if __name__=="__main__":
    print Solution().twoSum([3, 2, 4], 6)