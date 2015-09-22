"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
__author__ = 'Danyang'


class Solution(object):
    def reverse(self, x):
        """
        Sign for preserving negative number of positive number
        :param x: int
        :return: int
        """
        sign = -1 if x < 0 else 1  # preserve the sign first
        x *= sign

        # eliminated leading zero in the reversed integer
        while x:
            if x%10 == 0:
                x /= 10
            else:
                break

        # string manipulation
        x = str(x)
        lst = list(x)  # list('123') returns ['1', '2', '3']
        lst.reverse()
        x = "".join(lst)
        x = int(x)
        return sign*x


if __name__ == "__main__":
    print Solution().reverse(123)

