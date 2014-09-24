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
__author__ = 'Danyang'
class Solution:
    def minWindow(self, S, T):
        """
        Algorithm:
        two pointers

        Aggressively enclose the chars until find all T, and then shrink the window as far as possible
        :param S: str
        :param T: str
        :return: str
        """
        min_window = [0, 1<<32]  # start end
        w_chars = [0 for _ in range(256)]  # window
        t_chars = [0 for _ in range(256)]  # 256 ascii
        appeared_cnt = 0
        start_ptr = 0
        for char in T:
            t_chars[ord(char)] += 1

        for end_ptr in xrange(len(S)):
            # expand
            val = S[end_ptr]
            if t_chars[ord(val)]>0:
                w_chars[ord(val)] += 1
            if t_chars[ord(val)]>0 and w_chars[ord(val)]<=t_chars[ord(val)]:
                appeared_cnt += 1  # when to decrease appeared_cnt?

            # shrink
            if appeared_cnt==len(T):  # until find all
                # while w_chars[ord(S[start_ptr])]>t_chars[ord(S[start_ptr])] or w_chars[ord(S[start_ptr])]<=0:
                while w_chars[ord(S[start_ptr])]>t_chars[ord(S[start_ptr])] or t_chars[ord(S[start_ptr])]<=0:
                    w_chars[ord(S[start_ptr])] -= 1
                    start_ptr += 1

                if min_window[1]-min_window[0]>end_ptr-start_ptr+1:
                    min_window[0], min_window[1] = start_ptr, end_ptr+1

        if min_window[1]==1<<32:
            return ""
        return S[min_window[0]:min_window[1]]

if __name__=="__main__":
    print Solution().minWindow("ADOBECODEBANC", "ABC")