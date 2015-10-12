"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        Backtracking with prune
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        return self.dfs(pattern, s, {}, set())

    def dfs(self, pattern, s, char2word, words):
        """
        Loop & DFS
        :return: pattern can match s
        """
        if not pattern and s or not s and pattern:
            return False

        if not pattern and not s:
            return True


        if pattern[0] in char2word:
            word = char2word[pattern[0]]
            if s[:len(word)] != word:
                return False
            else:
                assert word in words
                return self.dfs(pattern[1:], s[len(word):], char2word, words)
        else:
            for i in xrange(len(s)):
                word = s[:i+1]
                if word in words:
                    continue

                char2word[pattern[0]] = word
                words.add(word)
                if self.dfs(pattern[1:], s[len(word):], char2word, words):
                    return True
                words.remove(word)
                del char2word[pattern[0]]

            return False