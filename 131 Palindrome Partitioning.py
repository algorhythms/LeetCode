__author__ = 'Danyang'
class Solution:
    def partition(self, s):
        """
        dfs
        :param s: string
        :return: a list of lists of string
        """
        result = []
        self.get_partition(s, [], result)
        return result

    def get_partition(self, s, cur_lst, result):
        if not s:
            result.append(cur_lst)
        # partition s
        for i in xrange(len(s)):
            if self.is_palindrome(s[:i+1]):  # otherwise prune 
                self.get_partition(s[i+1:], cur_lst+[s[:i+1]], result)


    def is_palindrome(self, s):
        # O(n)
        # return s==reversed(s)  # error, need to use ''.join(reversed(s))
        return s==s[::-1]

if __name__=="__main__":
    print Solution().partition("aab")