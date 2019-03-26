#!/usr/bin/python3
"""
We are given two arrays A and B of words.  Each word is a string of lowercase
letters.

Now, say that word b is a subset of word a if every letter in b occurs in a,
including multiplicity.  For example, "wrr" is a subset of "warrior", but is
not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order.



Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]


Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from typing import List
from collections import Counter, defaultdict


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        """
        brute foce check b subset of a: two pointers O(|a| + |b|)
        O(n * m * (|a|+|b|))

        The order of chars does not matter.

        For every letter
        C_letter (a) >= max(C_letter(b) for b in B)
        """
        mx = defaultdict(int)
        for b in B:
            c = Counter(b)
            for k, v in c.items():
                mx[k] = max(mx[k], v)

        ret = []
        for a in A:
            c = Counter(a)
            for k, v in mx.items():
                if c[k] < v:
                    break
            else:
                ret.append(a)

        return ret
