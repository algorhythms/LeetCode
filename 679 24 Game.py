#!/usr/bin/python3
"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether
they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For
example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a
unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is
[1, 2, 1, 2], we cannot write this as 12 + 12.
"""
from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.dfs(nums, {})

    def dfs(self, A, cache):
        if tuple(A) not in cache:
            n = len(A)
            if n == 1:
                return abs(A[0] - 24) < 0.001

            for i in range(n):
                for j in range(i):
                    a = A[i]
                    b = A[j]
                    for c in (a+b, a-b, b-a, a*b, b and a/b, a and b/a):
                        # if 0, duplicated as a * b 
                        A_new = A[:j] + A[j+1:i] + A[i+1:] + [c]
                        A_new.sort()
                        if self.dfs(A_new, cache):
                            cache[tuple(A)] = True
                            return cache[tuple(A)]

            cache[tuple(A)] = False

        return cache[tuple(A)]


if __name__ == "__main__":
    assert Solution().judgePoint24([4, 1, 8, 7]) == True
    assert Solution().judgePoint24([1, 2, 1, 2]) == False
