"""
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

For example:

Given s = "aabb", return ["abba", "baab"].

Given s = "abc", return [].
"""
from collections import defaultdict


__author__ = 'Daniel'


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        odd = None
        for k, v in m.items():
            if v % 2 == 1:
                if odd is not None:
                    return []
                odd = k

        cur = ""
        if odd:
            m[odd] -= 1
            cur = odd

        ret = []
        # actually only need to build half
        self.grow(s, m, None, cur, ret)
        return ret

    def grow(self, s, m, pi, cur, ret):
        if len(cur) == len(s):
            ret.append(cur)
            return

        for k in m.keys():
            if k != pi and m[k] > 0:
                for i in xrange(1, m[k]/2+1):
                    m[k] -= i*2
                    self.grow(s, m, k, k*i+cur+k*i, ret)
                    m[k] += i*2


if __name__ == "__main__":
    print Solution().generatePalindromes("aabb")