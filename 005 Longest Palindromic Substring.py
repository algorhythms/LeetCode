"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and
there exists one unique longest palindromic substring.
"""
__author__ = 'Danyang'
class Solution:
    def longestPalindrome_TLE(self, s):
        """
        Algorithm: dp, O(n^2)

        p[i,j] represents weather s[i:j] is palindrome. (incl. i-th while excl. j-th)
        For example S = "abccb"
                         01234
        p[0,1] = True, p[1,2] = True, etc. since single char is Palindrom
        p[0,2] = s[0]==s[1],
        p[0,3] = s[0]==s[2] && p[1,2]
        p[0,4] = s[0]==s[3] && p[1,3]
        p[0,5] = s[0]==s[4] && p[1,4]

        thus,
        p[i,j] = 1 if i+1==j
        p[i,j] = s[i]==s[j-1] if i+1==j-1 else
        p[i,j] = s[i]==s[j-1] && p[i+1, j-1]

        :param s: string
        :return: string
        """
        length = len(s)
        dp = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]

        longest = [0, 0]
        for j in xrange(length+1):
            for i in xrange(j-1, -1, -1):
                if i+1==j:
                    dp[i][j] = True
                elif i+1==j-1:
                    dp[i][j] = s[i]==s[j-1]
                else:
                    dp[i][j] = s[i]==s[j-1] and dp[i+1][j-1]  # pre-access? starting backward


                if dp[i][j]==True and longest[1]-longest[0]<j-i:
                    longest[0], longest[1] = i, j

        return s[longest[0]:longest[1]]

    def longestPalindrome(self, s):
        """
        :param s: string
        :return: string
        """
        # TODO

if __name__=="__main__":
    assert Solution().longestPalindrome("dfaaabbbaaac")=="aaabbbaaa"