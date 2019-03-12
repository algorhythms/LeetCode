#!/usr/bin/python3
"""
Given string S and a dictionary of words words, find the number of words[i] that
is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a",
"acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """
        Linear O(|S| + sum(|word|))
        no need to if-check

        HashMap + Iterator
        """
        itrs_m = defaultdict(list)
        for w in words:
            itrs_m[w[0]].append(
                iter(w[1:])
            )
        for a in S:
            itrs = itrs_m.pop(a, [])
            for itr in itrs:
                v = next(itr, None)
                itrs_m[v].append(itr)

        return len(itrs_m[None])

    def numMatchingSubseq_TLE(self, S: str, words: List[str]) -> int:
        """
        Brute force O(|S| |Words| M)

        Is a better way to check subsequence? No
        Can we parallel the works? Yes

        go through all words parallel
        O(|S| |Words|)
        """
        I = [0 for _ in words]
        for a in S:
            for wi, i in enumerate(I):
                if i < len(words[wi]) and words[wi][i] == a:
                    I[wi] += 1

        return sum(
            1
            for wi, i in enumerate(I)
            if i == len(words[wi])
        )


if __name__ == "__main__":
    assert Solution().numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]) == 3
