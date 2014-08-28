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
            # avoid duplicates
            if ind-1>=0 and val==S[ind-1]:
                continue
            self.get_subset(S[ind+1:], current+[val], result)


if __name__=="__main__":
    print Solution().subsetsWithDup([1, 2, 3])