"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""
__author__ = 'Danyang'


class Solution(object):
    def minCut(self, s):
        """
        Let P[i][j] indicates whether s[i:j] is palindrome
        P[i][j] = P[i+1][j-1] && s[i] == s[j-1]

        Left C[i] represents the min cut for s[:i]
        C[i] = 0 if s[:i] is palindrome
        C[i] = min(C[j]+1 for j<i if s[j:i] is palindrome)
        """
        n = len(s)

        P = [[False for _ in xrange(n+1)] for _ in xrange(n+1)]
        for i in xrange(n+1):  # len 0
            P[i][i] = True
        for i in xrange(n):  # len 1
            P[i][i+1] = True

        for i in xrange(n, -1, -1):  # len 2 and above
            for j in xrange(i+2, n+1):
                P[i][j] = P[i+1][j-1] and s[i] == s[j-1]

        C = [i for i in xrange(n+1)]  # initial values, max is all cut
        for i in xrange(n+1):
            if P[0][i]:
                C[i] = 0
            else:
                C[i] = min(
                    C[j] + 1
                    for j in xrange(i)
                    if P[j][i]
                )

        return C[n]

    def minCut_dp(self, s):
        """
        dp

        a   b   a   b   b   b   a   b   b   a   b   a
                    i                       k
        if s[i:k+1] is palindrome, #cut is 0; otherwise
        cut s[i:k+1] into palindrome, the #cut:
          cut the s[i:k+1] to two parts
          cut the left part into palindrome, #cut is dp[i, j]
          cut the right part into palindrome, #cut is dp[j+1, k+1]
        find the minimum for above

        dp[i, n+1] = min(dp[i, j]+dp[j, k+1]+1)

        when drawing the matrix, you will find it difficult to construct it at one shot (especially, vertical line)


        To avoid TLE, use 1-d dp instead of 2-d dp
        D[i] represents #cut for s[i:length+1]
        if s[i:j] is palindrome and we need #cut for s[j:] is D[j], then
        for minimum: D[i] = min(D[j+1]+1) for all j

        To avoid TLE, use dp for determination of palindrome
        Determine s[i:k+1] is palindrome:
        P[i, k+1] = P[i+1, k] && s[i]==s[k]

        * another algorithm is dfs with global_min
        * to tell s[i:k+1] whether it is palindrome can be optimized by dp
        :param s: str
        :return: int
        """
        if not s:
            return 0

        length = len(s)
        # palindrome dp
        P = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                P[i][i] = True
                P[i][i+1] = True
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for j in xrange(i+2, length+1):
                try:
                    P[i][j] = P[i+1][j-1] and s[i] == s[j-1]
                except IndexError:
                    P[i][j] = True

        # min cut dp
        D = [length-i-1 for i in xrange(length)]  # max is all cut
        for i in xrange(length-1, -1, -1):
            if P[i][length]:
                D[i] = 0
            else:
                for j in xrange(i+1, length):
                    if P[i][j]:
                        D[i] = min(D[i], D[j]+1)
        return D[0]

    def minCut_MLE(self, s):
        """
        bfs
        :param s: str
        :return: int
        """
        q = [[s]]
        count = -1
        while q:
            # cur = q.pop(0)  # not directly pop
            length = len(q)
            count += 1
            for cur_level in xrange(length):
                cur = q[cur_level]
                if all(self.is_palindrome(item) for item in cur):
                    return count
                # 1 cut
                for ind, val in enumerate(cur):
                    for i in xrange(1, len(val)):
                        cut1 = val[:i]
                        cut2 = val[i:]
                        new_cur = list(cur)
                        new_cur[ind] = cut1
                        new_cur.insert(ind+1, cut2)
                        q.append(new_cur)
            q = q[length:]

    def minCut_TLE(self, s):
        """
        dp

        a   b   a   b   b   b   a   b   b   a   b   a
                    i                       k
        if s[i:k+1] is palindrome, #cut is 0; otherwise
        cut s[i:k+1] into palindrome, the #cut:
          cut the s[i:k+1] to two parts
          cut the left part into palindrome, #cut is dp[i, j]
          cut the right part into palindrome, #cut is dp[j+1, k+1]
        find the minimum for above

        dp[i, n+1] = min(dp[i, j]+dp[j, k+1]+1)

        when drawing the matrix, you will find it difficult to construct it at one shot (especially, vertical line)

        * another algorithm is dfs with global_min
        * to tell s[i:k+1] whether it is palindrome can be optimized by dp
        :param s: str
        :return: int
        """
        if not s:
            return 0

        length = len(s)
        dp = [[1<<32-1 for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                dp[i][i] = 0
                dp[i][i+1] = 0
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for k in xrange(i, length+1):
                if self.is_palindrome(s[i:k]):
                    dp[i][k] = 0
                else:
                    dp[i][k] = min(1+dp[i][j]+dp[j][k] for j in xrange(i+1, k))

        return dp[0][length]

    def is_palindrome(self, s):
        return s == s[::-1]

    def minCut_TLE2(self, s):
        """
        dp

        a   b   a   b   b   b   a   b   b   a   b   a
                    i                       k
        if s[i:k+1] is palindrome, #cut is 0; otherwise
        cut s[i:k+1] into palindrome, the #cut:
          cut the s[i:k+1] to two parts
          cut the left part into palindrome, #cut is dp[i, j]
          cut the right part into palindrome, #cut is dp[j+1, k+1]
        find the minimum for above

        dp[i, n+1] = min(dp[i, j]+dp[j, k+1]+1)

        when drawing the matrix, you will find it difficult to construct it at one shot (especially, vertical line)


        Determine s[i:k+1] is palindrome:
        dp2[i, k+1] = dp2[i+1, k] && s[i]==s[k]

        * another algorithm is dfs with global_min
        * to tell s[i:k+1] whether it is palindrome can be optimized by dp
        :param s: str
        :return: int
        """
        if not s:
            return 0

        length = len(s)
        # palindrome dp
        dp2 = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                dp2[i][i] = True
                dp2[i][i+1] = True
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for j in xrange(i+2, length+1):
                try:
                    dp2[i][j] = dp2[i+1][j-1] and s[i] == s[j-1]
                except IndexError:
                    dp2[i][j] = True


        # min cut dp
        dp = [[1<<32-1 for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                dp[i][i] = 0
                dp[i][i+1] = 0
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for k in xrange(i, length+1):
                if dp2[i][k]:
                    dp[i][k] = 0
                else:
                    dp[i][k] = min(1+dp[i][j]+dp[j][k] for j in xrange(i+1, k))

        return dp[0][length]


if __name__ == "__main__":
    assert Solution().minCut("aabbc") == 2
    assert Solution().minCut(
        "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp") == 452