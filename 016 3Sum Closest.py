"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return
the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
__author__ = 'Danyang'
class Solution:
    def threeSumClosest(self, num, target):
        """
        Three pointers scanning algorithm
        Similar to 014 3Sum

        :param num: array
        :param target: target
        :return: sum of the three digits
        """
        min_distance = 1<<32
        num.sort()
        min_summation = 0

        for i, val in enumerate(num):
            j = i+1
            k = len(num)-1
            while j<k:
                lst = [val, num[j], num[k]]
                if min_distance>abs(target-sum(lst)):
                    min_summation = sum(lst)
                    if sum(lst)==target:
                        return min_summation
                    min_distance = abs(target-min_summation)
                elif sum(lst)>target:
                    k -= 1
                else:
                    j += 1
        return min_summation

if __name__=="__main__":
    print Solution().threeSumClosest([1, 1, 1, 1], 0)

