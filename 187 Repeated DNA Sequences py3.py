#!/usr/bin/python3
"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ret = set()
        seen = set()
        for i in range(len(s) - 10 + 1):
            sub = s[i:i+10]
            if sub in seen and sub not in ret:
                ret.add(sub)
            else:
                seen.add(sub)

        return list(ret)
