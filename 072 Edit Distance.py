"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
__author__ = 'Danyang'
class Solution:
    def minDistance(self, word1, word2):
        """
        dp: Wagner-Fischer algorithm
        http://en.wikipedia.org/wiki/Wagner-Fischer_algorithm

        Part of Natural Language Processing
        Algorithm:
        Addition at anywhere
        Deletion at anywhere
        Substitution at anywhere
        Edit: Substitution, Addition, Deletion. Degree of Freedom is high
        word1[:i] is string_1a
        word2[:j] is string_2b
        d[i][j] represents convert word1[:i] to word2[:j]
        Substitution:
         convert word1[:i-1] to word2[:j-1] is d[i-1][j-1], then substitutes word1[i-1] with word2[j-1]
        Addition:
         convert word1[:i] to word2[:j-1] is d[i][j-1], then appends word2[j-1] to word1
        Deletion:
         convert word1[:i-1] to word2[:j] is d[i-1][j-1], then deletes word1[i]

        int EditDistance(char s[1..m], char t[1..n])
           # For all i and j, d[i,j] will hold the Levenshtein distance between
           # the first i characters of s and the first j characters of t.
           # Note that d has (m+1)  x(n+1) values.
           let d be a 2-d array of int with dimensions [0..m, 0..n]

           for i in [0..m]
             d[i, 0] = i # the distance of any first string to an empty second string
           for j in [0..n]
             d[0, j] = j # the distance of any second string to an empty first string

           for j in [1..n]
             for i in [1..m]
               if s[i] = t[j] then
                 d[i, j] = d[i-1, j-1]       # no operation required
               else
                 d[i, j] = minimum of
                            (
                              d[i-1, j] + 1,  # a deletion     # convert a[:i-1] to b[:j], then delete the last item of a
                              d[i, j-1] + 1,  # an insertion   # convert a[:i] to b[:j-1], then insert the last item of b into a
                              d[i-1, j-1] + 1 # a substitution # convert a[:i-1] to b[:j-1], then substitute a's last item to b's
                            )

           return d[m,n]

        :param word1: String
        :param word2: String
        :return: integer
        """
        m = len(word1)
        n = len(word2)
        d = [[-1 for _ in xrange(n+1)] for _ in xrange(m+1)]


        for i in xrange(m+1):
            d[i][0] = i
        for j in xrange(n+1):
            d[0][j] = j


        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if word1[i-1]==word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j]= min(
                        d[i-1][j]+1,  # deletion
                        d[i][j-1]+1,  # insertion
                        d[i-1][j-1]+1  # substitution
                    )

        return d[-1][-1]


