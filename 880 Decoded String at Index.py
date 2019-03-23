#!/usr/bin/python3
"""
An encoded string S is given.  To find and write the decoded string to a tape,
the encoded string is read one character at a time and the following steps are
taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly
written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter
(1 indexed) in the decoded string.

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation:
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: S = "ha22", K = 5
Output: "h"
Explanation:
The decoded string is "hahahaha".  The 5th letter is "h".
Example 3:

Input: S = "a2345678999999999999999", K = 1
Output: "a"
Explanation:
The decoded string is "a" repeated 8301530446056247680 times.  The 1st letter is "a".


Note:

2 <= S.length <= 100
S will only contain lowercase letters and digits 2 through 9.
S starts with a letter.
1 <= K <= 10^9
The decoded string is guaranteed to have less than 2^63 letters.
"""


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        """
        walk backward
        """
        l = 0
        for s in S:
            if s.isdigit():
                l *= int(s)
            else:
                l += 1

        # walk backward
        for s in reversed(S):
            K %= l
            if K == 0 and s.isalpha():
                # K == l * n, return the last chr
                return s
            if s.isdigit():
                l //= int(s)
            else:
                l -= 1

        raise

    def decodeAtIndex_error(self, S: str, K: int) -> str:
        """
        don't generate the final string, too memory expensive
        two pointer

        understanding error, one digit will make the entire str repeated
        """
        K -= 1  # 0-indexed
        i = 0
        j = 0
        last = None
        n = len(S)
        while j < n:
            if S[j].isdigit():
                if not last:
                    last = j

                d = int(S[j])
                l = last - i
                while K >= l and d > 0:
                    K -= l
                    d -= 1
                if d > 0:
                    return S[i + K]
            elif last:
                    i = j
                    last = None

            j += 1

        return S[i+K]


if __name__ == "__main__":
    assert Solution().decodeAtIndex("ha22", 5) == "h"
