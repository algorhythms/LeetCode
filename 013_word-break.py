__author__ = 'Danyang'


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak_TLE(self, s, dict):
        """
        TLE
        O(n^2)
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
        """
        pass

if __name__=="__main__":
    print Solution().wordBreak("aaaaaaa", ["aaaa", "aaa"])