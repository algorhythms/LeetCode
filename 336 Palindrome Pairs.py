#!/usr/bin/python3
"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the
given list, so that the concatenation of the two words, i.e. words[i] + words[j]
is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
"""
from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.pali_prefix_idxes = []  # suffix ends, prefix pali
        self.word_idx = None
        self.children = defaultdict(TrieNode)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        Brute force, i, j and then check palindrom
        O(N^2 * L)

        Reverse the str, and then check O(N * L). Does it work actually?
        Check: map str -> idx

        |---s1---|---s2--|     |---s1---|-s2-|    |-s1-|---s2---|
        Need to check whether part of the str is palindrome.
        Part of str -> Trie.
        How to check part of the str. Useful

        Better way of checking palindrome? Infamouse Manacher

        word_i   | word_j
        abc pppp | cba
             abc | pppp cba

        If palindrome suffix in work_i, we only need to check the "abc" against word_j
        Similarly for palindrome prefix in word_j

        Construct Trie for word_j reversely, since word_j is being checked
        """
        root = TrieNode()
        for idx, w in enumerate(words):
            cur = root
            for i in range(len(w) - 1, -1, -1):
                #  cur.children[w[i]]  # error, pre-advancing the trie is unable to handle empty str
                if self.is_palindrome(w, 0, i + 1):
                    cur.pali_prefix_idxes.append(idx)

                cur = cur.children[w[i]]

            cur.pali_prefix_idxes.append(idx)  # empty str is palindrome
            cur.word_idx = idx  # word ends

        ret = []
        for idx, w in enumerate(words):
            cur = root
            for i in range(len(w)):
                # cur.children.get(w[i], None)  # error, pre-advancing the trie is unable to handle empty str
                if self.is_palindrome(w, i, len(w)) and cur.word_idx is not None and cur.word_idx != idx:
                    ret.append([idx, cur.word_idx])

                cur = cur.children.get(w[i], None)
                if cur is None:
                    break
            else:
                for idx_j in cur.pali_prefix_idxes:
                    if idx != idx_j:
                        ret.append([idx, idx_j])

        return ret

    def is_palindrome(self, w, lo, hi):
        i = lo
        j = hi - 1
        while i < j:
            if w[i] != w[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "__main__":
    assert Solution().palindromePairs(["a", ""]) == [[0,1],[1,0]]
    assert Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]) == [[0,1],[1,0],[2,4],[3,2]]
