#!/usr/bin/python3
"""
Consider the string s to be the infinite wraparound string of
"abcdefghijklmnopqrstuvwxyz", so s will look like this:
"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty
substrings of p are present in s. In particular, your input is the string p and
you need to output the number of different non-empty substrings of p in the
string s.

Note: p consists of only lowercase English letters and the size of p might be
over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string
"zab" in the string s.
"""


class Solution:
    def findSubstringInWraproundString(self, p):
        """
        wrap around: +1 (delta=1)
        "zab": 3 + 2 + 1
        "zabc": 4 + 3 + 2 + 1
        To de-dpulicate, change the way of counting - count backward at the
        ending char.
        "zabc":
            "z": "z" : 1
            "a": "a", "za": 2
            "zab": "b", "ab", "zab": 3
            "zabc": "c", ...: 4

        p.s. possible to count forward but tedious 
        :type p: str
        :rtype: int
        """
        counter = {
            c: 1
            for c in p
        }
        l = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:  # (0 - 25) % 26 == 1
                l += 1
            else:
                l = 1
            counter[p[i]] = max(counter[p[i]], l)

        return sum(counter.values())

    def findSubstringInWraproundString_error(self, p):
        """
        wrap around: +1 (delta=1)
        "zab": 3 + 2 + 1
        "zabc": 4 + 3 + 2 + 1
        :type p: str
        :rtype: int
        """
        if not p:
            return 0

        ret = set()
        i = 0
        while i < len(p):
            cur = [p[i]]
            j = i + 1
            while j < len(p) and (ord(p[j]) - ord(cur[-1]) == 1 or p[j] == "a" and cur[-1] == "z"):
                cur.append(p[j])
                j += 1
            ret.add("".join(cur))
            i = j

        return sum(map(lambda x: (len(x) + 1) * len(x) // 2, ret))


if __name__ == "__main__":
    assert Solution().findSubstringInWraproundString("a") == 1
    assert Solution().findSubstringInWraproundString("cac") == 2
    assert Solution().findSubstringInWraproundString("zab") == 6
    assert Solution().findSubstringInWraproundString("zaba") == 6
