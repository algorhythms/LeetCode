#!/usr/bin/python3
"""
Given a string S of digits, such as S = "123456579", we can split it into a
Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such
that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer
type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have
extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be
done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""
from typing import List


MAX = 2 ** 31 - 1


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        """
        The first two elements of the array uniquely determine the rest of the
        sequence.

        2^31 - 1 is length 10
        brute force
        """
        l = len(S)
        for i in range(1, l + 1):
            num_str = S[:i]
            if len(num_str) > 1 and num_str.startswith("0"):
                continue

            num = int(num_str)
            if num > MAX:
                break

            for j in range(i + 1, l + 1):
                num2_str = S[i:j]
                if len(num2_str) > 1 and num2_str.startswith("0"):
                    continue

                num2 = int(num2_str)
                if num2 > MAX:
                    break

                ret = [num, num2]
                k = j
                while k < l:
                    nxt = ret[-1] + ret[-2]
                    if nxt > MAX:
                        break

                    nxt_str = str(nxt)
                    if S[k:k+len(nxt_str)] == nxt_str:
                        k = k + len(nxt_str)
                        ret.append(nxt)
                    else:
                        break
                else:
                    if k == l and len(ret) >= 3:
                        return ret

        return []


if __name__ == "__main__":
    assert Solution().splitIntoFibonacci("123456579") == [123,456,579]
    assert Solution().splitIntoFibonacci("01123581321345589") == [0,1,1,2,3,5,8,13,21,34,55,89]
