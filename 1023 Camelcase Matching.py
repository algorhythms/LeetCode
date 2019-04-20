#!/usr/bin/python3
"""
A query word matches a given pattern if we can insert lowercase letters to the
pattern word so that it equals the query. (We may insert each character at any
position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where
answer[i] is true if and only if queries[i] matches the pattern.

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
"ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation:
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
"ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation:
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer",
"ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation:
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".

Note:
1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.
"""
from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        for q in queries:
            ret.append(self.match(q, pattern))
            
        return ret

    def match(self, q, p):
        i = 0
        j = 0
        while i < len(q) and j < len(p):
            if q[i] == p[j]:
                i += 1
                j += 1
            elif q[i].islower():
                i += 1
            else:
                break

        while i < len(q) and q[i].islower():
            i += 1

        return i == len(q) and j == len(p)


if __name__ == "__main__":
    assert Solution().camelMatch(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa") == [True, False, True, False, False]
