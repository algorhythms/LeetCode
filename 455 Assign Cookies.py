#!/usr/bin/python3
"""
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed
factor gi, which is the minimum size of a cookie that the child will be content
with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j
to the child i, and the child i will be content. Your goal is to maximize the
number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.
"""


class Solution:
    def findContentChildren(self, g, s):
        """
        Greedy

        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ret = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ret += 1
                i += 1
                j += 1
            else:
                j += 1

        return ret


if __name__ == "__main__":
    assert Solution().findContentChildren([10,9,8,7], [5,6,7,8]) == 2
