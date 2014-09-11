"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
__author__ = 'Danyang'
class Solution:
    def restoreIpAddresses(self, s):
        """
        dfs, branch factor 3, depth 4
        complexity: 3^4 = 81
        :param s: String
        :return: list of strings
        """
        result = []
        self.dfs(s, [], result)
        return result

    def dfs(self, seq, cur, result):
        if len(cur)>4:
            return

        if not cur or self.is_valid(cur[-1]):
            if len(cur)==4 and not seq:  # check the last one first
                result.append(".".join(cur))
                return

            for i in xrange(1, min(3, len(seq))+1):
                self.dfs(seq[i:], cur+[seq[:i]], result)


    def is_valid(self, s):
        return s=="0" or s[0]!="0" and 0<=int(s)<256  # ["0.0.0.0"]

if __name__=="__main__":
    print Solution().restoreIpAddresses("25525511135")