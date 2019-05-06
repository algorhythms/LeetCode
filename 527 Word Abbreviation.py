#!/usr/bin/python3
"""
premium question
"""

from typing import List
from collections import defaultdict


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        """
        Sort the word, check prefix and last word

        Group by first and last char, group by prefix and last char
        then make a trie - hard to implement? TrieNode lambda

        Need to count the #appearances in the TrieNode
        """
        hm = defaultdict(list)
        ret = [None for _ in words]
        for i, w in enumerate(words):
            hm[w[0], w[-1], len(w)].append(i)

        TrieNode = lambda: defaultdict(TrieNode)

        for lst in hm.values():
            root = TrieNode()
            for i in lst:
                w = words[i]
                cur = root
                for c in w:
                    cur = cur[c]
                    cur["count"] = cur.get("count", 0) + 1

            for i in lst:
                w = words[i]
                prefix_l = 0
                cur = root
                for c in w:
                    prefix_l += 1
                    cur = cur[c]
                    if cur["count"] == 1:
                        break

                ret[i] = self.abbrev(w, prefix_l)

        return ret

    def abbrev(self, w, prefix_l):
        abbrev_l = len(w) - 2 - prefix_l + 1
        if abbrev_l > 1:
            return w[:prefix_l] + str(abbrev_l) + w[-1]
        return w


if __name__ == "__main__":
    assert Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]) == ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
