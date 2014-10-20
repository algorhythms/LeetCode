"""
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
__author__ = 'Danyang'
class Solution:
    def subsetsWithDup(self, S):
        """
        dfs
        notice the skipping
        :param S: a list of integer
        :return: a list of lists of integer
        """
        S.sort()
        result = []
        self.get_subset(S, [], result)
        return result

    def get_subset(self, S, current, result):
        result.append(current)
        for ind, val in enumerate(S):
            # JUMP, avoid duplicates
            if ind-1>=0 and val==S[ind-1]:  # ensure uni-direction
                continue
            self.get_subset(S[ind+1:], current+[val], result)


if __name__=="__main__":
    print Solution().subsetsWithDup([1, 2, 3])