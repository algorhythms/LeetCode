"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity
O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
import sys

__author__ = 'Danyang'


class Solution(object):
    def minWindow(self, S, T):
        """
        Algorithm:
        two pointers

        Aggressively enclose the chars until find all T, and then shrink the window as far as possible
        :param S: str
        :param T: str
        :return: str
        """
        min_win = [0, sys.maxint]  # [start, end)
        w_cnt = [0 for _ in range(256)]  # window
        t_cnt = [0 for _ in range(256)]  # 256 ascii, static
        for char in T:
            t_cnt[ord(char)] += 1

        appeared_cnt = 0
        lo = 0
        for hi in xrange(1, len(S)+1):
            # expand
            val = S[hi-1]
            if t_cnt[ord(val)] > 0:
                w_cnt[ord(val)] += 1

            if t_cnt[ord(val)] > 0 and w_cnt[ord(val)] <= t_cnt[ord(val)]:
                appeared_cnt += 1  # cache, determine when to decrease appeared_cnt

            # shrink
            if appeared_cnt == len(T):  # until find all
                while w_cnt[ord(S[lo])] > t_cnt[ord(S[lo])] or t_cnt[ord(S[lo])] == 0:
                    if w_cnt[ord(S[lo])] > 0: w_cnt[ord(S[lo])] -= 1
                    lo += 1

                if min_win[1]-min_win[0] > hi-lo:
                    min_win[0], min_win[1] = lo, hi

        if min_win[1] == sys.maxint:
            return ""
        else:
            return S[min_win[0]:min_win[1]]


if __name__ == "__main__":
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"