"""
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only
once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
"""
__author__ = 'Daniel'


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_pos = [-1 for _ in xrange(26)]
        n = len(s)
        for i in xrange(n-1, -1, -1):
            if last_pos[self._idx(s[i])] == -1:
                last_pos[self._idx(s[i])] = i

        stk = []
        stk_set = set()
        for i in xrange(n):
            v = s[i]
            if v not in stk_set:
                while stk and stk[-1] > v and last_pos[self._idx(stk[-1])] > i:
                    p = stk.pop()
                    stk_set.remove(p)
                stk.append(v)
                stk_set.add(v)

        return "".join(stk)

    def _idx(self, x):
        return ord(x) - ord('a')


if __name__ == "__main__":
    assert Solution().removeDuplicateLetters("cbacdcbc") == "acdb"