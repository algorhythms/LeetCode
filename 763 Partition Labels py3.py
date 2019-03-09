#!/usr/bin/python3
"""
A string S of lowercase letters is given. We want to partition this string into
as many parts as possible so that each letter appears in at most one part, and
return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits
S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lasts = {}
        n = len(S)
        for i in range(n-1, -1, -1):
            if S[i] not in lasts:
                lasts[S[i]] = i

        indexes = [-1]  # last partition ending index
        cur_last = 0
        for i in range(n):
            cur_last = max(cur_last, lasts[S[i]])
            if cur_last == i:
                indexes.append(cur_last)

        ret = []
        for i in range(len(indexes) - 1):
            ret.append(indexes[i+1] - indexes[i])
        return ret


if __name__ == "__main__":
    assert Solution().partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
