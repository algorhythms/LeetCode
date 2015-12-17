"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share
common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return
0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
"""
__author__ = 'Daniel'


class Solution(object):
    def maxProduct(self, words):
        """
        Brute force: O(n*n*k)
        Encode string using bit manipulation
        :type words: List[str]
        :rtype: int
        """
        l = map(len, words)
        codes = map(self.encode, words)
        maxa = 0
        for i in xrange(len(codes)):
            for j in xrange(i+1, len(codes)):
                if codes[i] & codes[j] == 0:
                    maxa = max(maxa, l[i]*l[j])

        return maxa

    def encode(self, x):
        ret = 0
        for c in x:
            ret |= 1 << (ord(c)-ord('a'))
        return ret


if __name__ == "__main__":
    assert Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16