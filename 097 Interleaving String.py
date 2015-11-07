"""
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
"""
__author__ = 'Danyang'


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        dfs
        dp

        dp[i][j], for s3[:i+j] interleaved by s1[:i], s2[:j]

          - d b b c a
        - T F F F F F
        a T F F F F F
        a T T T T T F
        b F T T F T F
        c F F T T T T
        c F F F T F T

        notice the boundary condition


        Thought:
        dfs, easy to come up, but high space complexity
        thus, dp
        f[i][j] represents s3[:i+j] comes from s1[:i] and s2[:j]
        two possible conditions:
        1. s[i+j] = s[i]
        2. s[i+j] = s[j]
        others are false

        f[i][j] = f[i-1][j] if s3[i+j]==s1[i]
                = f[i][j-1] if s3[i+j]==s2[j]
                = false

        :type s1: str
        :type s2: str
        :type s3: str
        :param s1:
        :param s2:
        :param s3:
        :return: boolean
        """
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False

        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]

        # initialize boundary conditions
        dp[0][0] = True
        for i in xrange(1, m+1):
            dp[i][0] = dp[i-1][0] and s3[i+0-1] == s1[i-1]
        for j in xrange(1, n+1):
            dp[0][j] = dp[0][j-1] and s3[0+j-1] == s2[j-1]

        # calculating
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if not dp[i][j]:
                    dp[i][j] = dp[i-1][j] and s3[i+j-1] == s1[i-1]
                if not dp[i][j]:
                    dp[i][j] = dp[i][j-1] and s3[i+j-1] == s2[j-1]

        return dp[-1][-1]

    def isInterleave_TLE(self, s1, s2, s3):
        """
        dfs
        Time Limit Exceeded
        :param s1:
        :param s2:
        :param s3:
        :return: boolean
        """
        if not s3:
            return True
        letter = s3[0]
        if s1 and s1[0] == letter:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return True
        if s2 and s2[0] == letter:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return True
        return False


if __name__ == "__main__":
    assert Solution().isInterleave("aa", "ab", "abaa") == True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac") == True
    assert Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc") == False