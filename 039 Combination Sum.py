"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
"""
__author__ = 'Danyang'
class Solution:
    def combinationSum(self, candidates, target):
        """
        dfs

        Notice that possible to repeat
        :param candidates: a lis of integers
        :param target: target, integer
        :return: a list of lists of integers
        """
        candidates.sort()
        result = []
        self.get_combination(target, candidates, [], result)
        return result

    def get_combination(self, target, candidates, current, result):
        if not candidates or sum(current)>target:
            return
        if sum(current)==target:
            result.append(current)
            return

        # add one of from the candidates
        for ind, val in enumerate(candidates):
            self.get_combination(target, candidates[ind:], current+[val], result)  # candidates[ind:] since possible repeat



if __name__=="__main__":
    print Solution().combinationSum([2,3,6,7], 7)