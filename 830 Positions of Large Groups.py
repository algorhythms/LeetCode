#!/usr/bin/python3
"""
In a string S of lowercase letters, these letters form consecutive groups of the
same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx",
"z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting
and ending positions of every large group.

The final answer should be in lexicographic order.



Example 1:

Input: "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the single large group with starting  3 and ending
positions 6.
Example 2:

Input: "abc"
Output: []
Explanation: We have "a","b" and "c" but no large group.
Example 3:

Input: "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]

Note:  1 <= S.length <= 1000
"""
from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i = 0
        j = 0
        ret = []
        n = len(S)
        while j < n:
            while j < n and S[i] == S[j]:
                j += 1
            if j - i >= 3:
                ret.append([i, j - 1])
            i = j

        return ret 
