__author__ = 'Danyang'


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak_TLE(self, s, dict):
        """
        TLE
        O(n^2)
        Algorithm: DFS. The reason is that DFS repeatly calculate whether a certain part of string can be segmented.
        Therefore we can use dynamic programming.
        """
        string_builder = ""
        if s=="":
            return True

        # greedy
        for i in range(len(s)):
            string_builder += s[i]
            if string_builder in dict:
                try:
                    if self.wordBreak_TLE(s[i+1:], dict):
                        return True
                    else:
                        continue
                except IndexError:
                    return True

        return False

    def wordBreak(self, s, dict):
        """
        Dynamic programming
        The dynamic solution can tell us whether the string can be broken to words, but can not tell us what words the string is broken to.

        O(n*m)
        """
        state = [False] * (len(s)+1)
        state[0] = True # dummy

        for i in range(len(s)):
            # continue from matched condition
            if state[i]==False:
                continue

            for word in dict:
                try:
                    # trival
                    if state[i+len(word)]==True:
                        continue

                    # main
                    if s[i:i+len(word)]==word: # test whether [i, i+len) can construct a word
                        state[i + len(word)] = True  # record the checking
                except IndexError:
                    continue

        return state[-1]



if __name__=="__main__":
    print Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"])