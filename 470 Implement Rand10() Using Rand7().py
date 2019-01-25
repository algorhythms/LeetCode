#!/usr/bin/python3
"""
Given a function rand7 which generates a uniform random integer in the range 1
to 7, write a function rand10 which generates a uniform random integer in the
range 1 to 10.

Do NOT use system's Math.random().
"""


# The rand7() API is already defined for you.
def rand7():
    return 0


class Solution:
    def rand10(self):
        """
        generate 7 twice, (rv1, rv2), 49 combination
        assign 40 combinations for the 1 to 10 respectively

        7-ary system
        :rtype: int
        """
        while True:
            rv1 = rand7()
            rv2 = rand7()
            s = (rv1 - 1) * 7 + (rv2 - 1)  # make it start from 0
            if s < 40:   # s \in [0, 40)
                return s % 10 + 1  # since I make it start from 0
