#!/usr/bin/python3
"""
Given a string, sort it in decreasing order based on the frequency of characters.
"""
from collections import defaultdict


class Solution(object):
    def frequencySort(self, s):
        """
        Brute force: counter, sort O(n log n)

        There is a uppper limit of the counter, thus bucket sort possible
        :type s: str
        :rtype: str
        """
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        bucket = {count: [] for count in range(1, len(s)+1)}
        for k, v in counter.items():
            bucket[v].append(k)

        ret = []
        for count in reversed(range(1, len(s) + 1)):
            if bucket[count]:
                for c in bucket[count]:
                    ret.append(c * count)

        return "".join(ret)


if __name__ == "__main__":
    assert Solution().frequencySort("tree") == "eetr"
