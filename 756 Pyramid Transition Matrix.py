#!/usr/bin/python3
"""
We are stacking blocks to form a pyramid. Each block has a color which is a one
letter string.

We are allowed to place any color block C on top of two adjacent blocks of
colors A and B, if and only if ABC is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also
start with a list of allowed triples allowed. Each allowed triple is represented
as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:

Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.
Similarly, we can place E on top of C and D, then A on top of G and E.


Example 2:

Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.


Note:

bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
'F', 'G'}.
"""
import itertools
from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        Need search, since multiple placements are possible
        The order of allowed matters
        """
        T = defaultdict(set)  # transition matrix
        for a, b, c in allowed:
            T[a, b].add(c)

        return self.dfs(T, bottom)

    def dfs(self, T, level) -> bool:
        if len(level) == 1:
            return True

        # for nxt_level in self.gen_nxt_level(T, level, 0):
        for nxt_level in itertools.product(
            *[T[a, b] for a, b in zip(level, level[1:])]
        ):
            if self.dfs(T, nxt_level):
                return True

        return False

    def gen_nxt_level(self, T, level, lo):
        """
        equiv to itertools.product - nested for-loops in a generator expression
        Cartesian product
        """
        if lo + 1 >= len(level):
            yield ""
            return

        for head in T[level[lo], level[lo + 1]]:
            for tail in self.gen_nxt_level(T, level, lo + 1):
                yield head + tail


    def dfs_deep(self, T, level, lo, nxt_level) -> bool:
        if lo + 1 == len(level):
            return True

        for nxt in T[level[lo], level[lo + 1]]:
            nxt_level.append(nxt)
            if self.dfs(T, level, lo + 1, nxt_level):
                # Too deep - check till top
                if self.dfs(T, nxt_level, 0, []):
                    return True
            nxt_level.pop()

        return False


if __name__ == "__main__":
    assert Solution().pyramidTransition("BCD", ["BCG", "CDE", "GEA", "FFF"]) == True
    assert Solution().pyramidTransition("AABA", ["AAA", "AAB", "ABA", "ABB", "BAC"]) == False
