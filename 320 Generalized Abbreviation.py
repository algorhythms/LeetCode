"""
Premium Question
Backtracking
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def generateAbbreviations(self, word):
        """
        backtracking, pivoting letter
        :type word: str
        :rtype: List[str]
        """
        if not word:
            return [""]

        ret = []
        for i in xrange(len(word)+1):
            left_num = str(i) if i else ""
            for right in self.generateAbbreviations(word[i+1:]):
                cur = left_num + word[i:i+1] + right
                ret.append(cur)

        return ret


class SolutionTLE(object):
    def __init__(self):
        self.cache = defaultdict(list)

    def generateAbbreviations(self, word):
        """
        Cached, brute force
        Two-way backtracking, pivoting number
        :type word: str
        :rtype: List[str]
        """
        return list(set(self.dfs(word)))

    def dfs(self, word):
        if word not in self.cache:
            ret = []
            for l in xrange(1, len(word)+1):
                pivot = str(l)
                for i in xrange(len(word)-l+1):
                    lefts = self.dfs(word[:i])
                    rights = self.dfs(word[i+l:])
                    for left in lefts:
                        for right in rights:
                            if left and left[-1].isdigit() or right and right[0].isdigit():
                                continue

                            ret.append(left+pivot+right)

            ret.append(word)
            self.cache[word] = ret

        return self.cache[word]


if __name__ == "__main__":
    assert Solution().generateAbbreviations("word") == ['word', 'wor1', 'wo1d', 'wo2', 'w1rd', 'w1r1', 'w2d', 'w3',
                                                        '1ord', '1or1', '1o1d', '1o2', '2rd', '2r1', '3d', '4']