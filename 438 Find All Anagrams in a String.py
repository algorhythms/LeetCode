#!/usr/bin/python3
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.
"""
from collections import Counter


class Solution:
    def findAnagrams(self, s, target):
        """
        Brute force: O(|target|) * O(cmp) * O(|s|)
        Counter: O(cmp) * O(|s|)
        where O(cmp) = 26, the length of alphabeta
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ret = []
        counter_target = Counter(target)
        counter_cur = Counter(s[:len(target)])
        if counter_cur == counter_target:
            ret.append(0)

        for idx in range(len(target), len(s)):
            head = s[idx - len(target)]
            tail = s[idx]
            counter_cur[tail] += 1
            counter_cur[head] -= 1
            if counter_cur[head] == 0:
                del counter_cur[head]  # requried for comparison
            if counter_cur == counter_target:
                # idx is the ending index, find the starting
                ret.append(idx - len(target) + 1)

        return ret


if __name__ == "__main__":
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
