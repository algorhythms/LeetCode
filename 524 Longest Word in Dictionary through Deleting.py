#!/usr/bin/python3
"""
Given a string and a string dictionary, find the longest string in the
dictionary that can be formed by deleting some characters of the given string.
If there are more than one possible results, return the longest word with the
smallest lexicographical order. If there is no possible result, return the empty
string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
from collections import defaultdict


class Solution:
    def findLongestWord(self, s, d):
        """
        Compare subsequence: O(|S|) (two pointers)
        Then iterate d, check subsequence: O(|S||d|)

        Generalize two pointers to n pointers
        O(|S||d|)


        :type s: str
        :type d: List[str]
        :rtype: str
        """
        h = defaultdict(list)
        for d_idx, w in enumerate(d):
            w_idx = 0
            h[w[w_idx]].append((d_idx, w_idx))

        ret = ""
        for e in s:
            lst = h.pop(e, [])
            for d_idx, w_idx in lst:
                w = d[d_idx]
                w_idx += 1
                if w_idx >= len(w):
                    # if len(w) >= len(ret) and w < ret:  # error
                    ret = min(ret, w, key=lambda x: (-len(x), x))  # compare with primary and secondary key
                else:
                    h[w[w_idx]].append((d_idx, w_idx))

        return ret


if __name__ == "__main__":
    assert Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]) == "apple"
