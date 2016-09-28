"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
__author__ = 'Daniel'


class Solution(object):
    def findNthDigit(self, n):
        """
        Math, quotient and remainder
        :type n: int
        :rtype: int
        """
        digit_cnt = 1
        num_cnt = 9
        while n > digit_cnt * num_cnt:
            n -= digit_cnt * num_cnt
            digit_cnt += 1
            num_cnt *= 10

        n -= 1  # debugging: without -1, it just pass over the target digit
        q, r = n / digit_cnt, n % digit_cnt
        target = num_cnt / 9 + q
        return int(str(target)[r])
