#!/usr/bin/python3
"""
Given a list of words (without duplicates), please write a program that returns
all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at
least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat",
"ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.
"""
from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        TrieNode = lambda: defaultdict(TrieNode)  # not defaultdict(lambda: TrieNode)
        self.root = TrieNode()  # root of tire

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Trie + DFS
        """
        words.sort(key=len)
        ret = []
        for w in words:
            if self.can_concat(w, 0):
                ret.append(w)

            cur = self.root
            for c in w:
                cur = cur[c]
            cur["end"] = True

        return ret

    def can_concat(self, word, lo):
        if not word:
            return False

        k = len(word)
        if lo >= k:
            return True

        cur = self.root
        for i in range(lo, k):
            cur = cur[word[i]]
            if cur.get("end", False) and self.can_concat(word, i + 1):
                return True

        return False


class SolutionTLE:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        """
        Trie check cannot be greedy: cat sdog vs cats dog

        Sort + Trie dfs
        What is the complexity?

        Word break DP
        for a specific word
        F[i] means word[:i] can be formed using shorter words

        complexity
        O(n) * O(k^2) * O(k)
        n words * get F * compare words

        Hard question is solving a collections of medium problems
        """
        ret = []
        # words.sort()  # sorting is unnecessary
        visited = set(words)
        for w in words:
            if self.can_concat(w, visited):
                ret.append(w)

        return ret

    def can_concat(self, w, visited):
        if not w:
            return False

        k = len(w)
        F = [False for _ in range(k + 1)]
        F[0] = True
        for i in range(1, k + 1):
            for j in range(i):
                if j == 0 and i == k:
                    continue  # word itself
                if F[j] and w[j:i] in visited:
                    F[i] = True

        return F[k]


if __name__ == "__main__":
    assert Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]) == ["catsdogcats","dogcatsdog","ratcatdogcat"]
