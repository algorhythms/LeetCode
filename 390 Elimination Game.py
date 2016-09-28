"""
There is a list of sorted integers from 1 to n. Starting from left to right, remove the first number and every other
number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number
from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length n.

Example:

Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
"""
__author__ = 'Daniel'


class Solution(object):
    def lastRemaining(self, n):
        """
        Brute force O(n): A = A[::2][::-1]

        Simulate the game and find pattern of head/first element: O(lg n)
        :type n: int
        :rtype: int
        """
        remain = n
        head = 1
        step = 1
        from_left = True
        while remain > 1:
            if from_left:
                head += step
            elif remain % 2 == 1:
                head += step

            step *= 2
            remain /= 2
            from_left = not from_left

        return head
