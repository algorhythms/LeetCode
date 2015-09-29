"""
Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        Sliding Window
        :type s: str
        :rtype: int
        """
        m = defaultdict(int)
        i = 0
        j = 0
        maxa = 0
        for j in xrange(len(s)):
            m[s[j]] += 1
            while len(m) > 2:
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    del m[s[i]]

                i += 1

            maxa = max(maxa, j-i+1)

        return maxa


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstringTwoDistinct("ecebaaaaaacdbb") == 7