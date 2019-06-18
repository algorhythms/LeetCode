#!/usr/bin/python3
"""
Given a positive integer N, how many ways can we write it as a sum of consecutive
positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3
Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
Note: 1 <= N <= 10 ^ 9.
"""


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        """
        Arithmetic Array
        math

        (x0 + xn) * (xn - x0 + 1) / 2 = N
        xn = x0 + k - 1
        (2x0 + k - 1) * k / 2 = N
        2x0 = 2N / k - k + 1

        x0 * k = N - k * (k - 1) / 2
        # assure for divisibility
        """
        cnt = 0
        k = 0
        while True:
            k += 1
            x0k = N - k * (k - 1) // 2
            if x0k <= 0 :
                break
            if x0k % k == 0:
                cnt += 1

        return cnt

    def consecutiveNumbersSum_error(self, N: int) -> int:
        """
        Arithmetic Array
        math

        (x0 + xn) * (xn - x0 + 1) / 2 = N
        xn = x0 + k - 1
        (2x0 + k - 1) * k / 2 = N
        2x0 = 2N / k - k + 1

        x0 * k = N - k * (k - 1) / 2
        # assure for divisibility
        """
        cnt = 0
        for k in range(1, int(N ** 0.5)):  # error
            x0k = N - k * (k - 1) // 2
            if x0k % k == 0:
                cnt += 1

        return cnt

    def consecutiveNumbersSum_error(self, N: int) -> int:
        """
        factor related
        9 / 3 = 3
        """
        if N == 1:
            return 1

        cnt = 0
        for i in range(1, N):
            d = N // i
            r = N % i
            if r == 0 and d - i // 2 > 0:
                cnt += 1
            elif r == 1 and N == (d + d + 1) * i // 2:
                cnt += 1
        return cnt
