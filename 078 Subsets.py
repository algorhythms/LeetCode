"""
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
__author__ = 'Danyang'
class Solution:
    def subsets(self, S):
        """
        Similar to permutation and combinations
        :param S: a list of integer
        :return: a list of lists of integer
        """
        S.sort()
        result = []
        self.generate_subsets(S, [], result)
        return result

    def generate_subsets(self, S, current, result):
        result.append(current)
        for ind, val in enumerate(S):
            self.generate_subsets(S[ind+1:], current+[val], result)

if __name__=="__main__":
    print Solution().subsets([1, 2, 3])