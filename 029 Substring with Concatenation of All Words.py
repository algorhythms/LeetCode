"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of
substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
__author__ = 'Danyang'
class Solution:
    def findSubstring_TLE(self, S, L):
        """
        Time limit exceeded

        Algorithm
        1. brutal force scanning: O(n*(l*k))
        2. sliding window: O(n*k)
        n: len(S)
        l: len(L)
        k: len(L[0])

        :param S: String
        :param L: a list of string
        :return: a list of integer
        """
        if not L:
            return

        k = len(L[0])
        l = len(L)

        working_list = list(L)
        result = []
        window_t = -1  # [0, t)
        window = []
        i = 0
        while i<=len(S)-3:
            # test window
            if len(window)==l:
                result.append(window_t-l*k)

            word = S[i:i+3]
            if word in working_list:
                window.append(word)
                working_list.remove(word)
                window_t = i+3
                i += 3

            elif word not in L:
                if window:
                    i = window_t-len(window)*k+1  # going to original point plus 1
                else:
                    i += 1

                window = []
                window_t = -1
                working_list = list(L)


            elif word in L and word not in working_list:
                window = window[window.index(word)+1:]
                window.append(word)
                # working_list.remove(word)
                window_t = i+3
                i += 3

        return result

    def findSubstring(self, S, L):
        """
        Algorithm
        1. brutal force scanning: O(n*(l*k)), rechecking
        2. sliding window: O(n*k)
        n: len(S)
        l: len(L)
        k: len(L[0])

        S = a1a3a2a1a3a4a5
        L = a1a2a3

        [a1a3a2]a1a3a4a5
        a1[a3a2a1]a3a4a5
        a1a3[a2a1a3]a4a5

        Notice:
        1. notice "aaaaaaaa" ["aa", "aa", "aa"]; sometimes cannot jump the whole word

        :param S: String
        :param L: a list of string
        :return: a list of integer
        """
        if not L:
            return

        k = len(L[0])
        l = len(L)

        Lmap = {}  # map of L
        for item in L:
            if item in Lmap:
                Lmap[item] += 1
            else:
                Lmap[item] = 1

        Lmap_original = dict(Lmap)

        ret = []
        win_e = -1  # [0, t), no need start_ptr
        working_win = []
        i = 0
        while i<len(S):
            # test window
            if len(working_win)==l:
                ret.append(win_e-l*k)
                candidate = win_e-l*k+1
                if S[candidate:candidate+k] in Lmap:
                    win_e = -1
                    i = candidate
                    Lmap = dict(Lmap_original)
                    working_win = []

            word = S[i:i+k]
            # case 1, match one in L
            if word in Lmap and Lmap[word]>0:
                working_win.append(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

            # case 2, no match
            elif word not in Lmap:
                if working_win:
                    i = win_e-len(working_win)*k+1  # going to window start+1  # cannot jump
                else:
                    i += 1

                working_win = []
                win_e = -1
                Lmap = dict(Lmap_original)

            # case 3, mach one in L not used up
            elif word in Lmap and Lmap[word]==0:
                for j in xrange(0, working_win.index(word)+1):  # kind of prefix suffix concepts
                    Lmap[working_win[j]] += 1  # restore
                working_win = working_win[working_win.index(word)+1:]
                working_win.append(word)
                Lmap[word] -= 1
                win_e = i+k
                i += k

        if len(working_win)==l:  # when reaching the end, assert Solution().findSubstring("a", ["a"])==[0]
            ret.append(win_e-l*k)

        return ret

if __name__=="__main__":
    assert Solution().findSubstring("abababab", ["a","b","a"])==[0,2,4]
    assert Solution().findSubstring("a", ["a"])==[0]
    assert Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"])==[13]
    assert Solution().findSubstring("barfoofoofoobarman", ["foo", "foo"])==[3, 6]
