#!/usr/bin/python3
"""
A gene string can be represented by an 8-character long string, with choices
from "A", "C", "G", "T".

Suppose we need to investigate about a mutation (mutation from "start" to
"end"), where ONE mutation is defined as ONE single character changed in the
gene string.

For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.

Also, there is a given gene "bank", which records all the valid gene mutations.
A gene must be in the bank to make it a valid gene string.

Now, given 3 things - start, end, bank, your task is to determine what is the
minimum number of mutations needed to mutate from "start" to "end". If there is
no such a mutation, return -1.

Note:

Starting point is assumed to be valid, so it might not be included in the bank.
If multiple mutations are needed, all mutations during in the sequence must be
valid.
You may assume start and end string is not the same.
"""


class Solution:
    def is_neighbor(self, p, q):
        diff = 0
        for a, b in zip(p, q):
            if a != b:
                diff += 1
            if diff > 1:
                return False
        return True

    def minMutation(self, start, end, bank):
        """
        BFS, record level and avoid loop

        Similar to 127 Word Ladder

        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        q = [start]
        visited = {start}
        lvl = 0
        while q:
            cur_q = []
            for e in q:
                if e == end:
                    return lvl
                for t in bank:
                    if t not in visited and self.is_neighbor(e, t):
                        visited.add(t)
                        cur_q.append(t)

            lvl += 1
            q = cur_q

        return -1


if __name__ == "__main__":
    assert Solution().minMutation("AACCTTGG", "AATTCCGG", ["AATTCCGG","AACCTGGG","AACCCCGG","AACCTACC"]) == -1
    assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
