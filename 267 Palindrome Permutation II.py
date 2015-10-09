"""
Premium Question
https://leetcode.com/problems/palindrome-permutation-ii/
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

    def grow(self, s, count_map, pi, cur, ret):
        if len(cur) == len(s):
            ret.append(cur)
            return

        for k in count_map.keys():
            if k != pi and count_map[k] > 0:
                for i in xrange(1, count_map[k]/2+1):  # jump the parent
                    count_map[k] -= i*2
                    self.grow(s, count_map, k, k*i+cur+k*i, ret)
                    count_map[k] += i*2


if __name__ == "__main__":
    assert Solution().generatePalindromes("aabb") == ['baab', 'abba']