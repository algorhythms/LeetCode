"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep
"shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting
sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Return:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
Note: For the return value, each inner list's elements must follow the lexicographic order.
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution:
    def groupStrings(self, strings):
        """

        :type strings: list[str]
        :rtype: list[list[str]]
        """
        hm = defaultdict(list)
        for s in strings:
            if len(s) == 1:
                hm[0].append(s)
            else:
                lst = []
                for i in xrange(1, len(s)):
                    lst.append((ord(s[i])-ord(s[i-1]))%26)
                hm[tuple(lst)].append(s)

        return map(sorted, hm.values())