"""
Your task is to calculate a^b mod 1337 where a is a positive integer and b is an extremely large positive integer given
in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024
"""
__author__ = 'Daniel'

C = 1337


class Solution(object):
    def superPow(self, a, b):
        """
        since b is given as a list rather than a number, we need to process it digit by digit.

        a^123 = a^120 * a^3
              = a^12 ^ 10 * a^3

        Power math.
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        s = 1
        lsd = b.pop()  # list significant digit
        s *= (a % C) ** lsd
        s %= C
        rest = self.superPow(a, b)
        s *= rest ** 10
        s %= C
        return s

if __name__ == "__main__":
    print Solution().superPow(2, [1, 0])




