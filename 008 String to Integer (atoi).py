"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself
what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather
all the input requirements up front.
"""
__author__ = 'Danyang'


class Solution:
    def atoi(self, str):
        """
        Need to satisfy all the nuance requirements

        :param str: string
        :return: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # clean
        str = str.strip()
        if not str:
            return 0

        # clean up leading sign
        sign = 1
        if str[0] in ("+", "-"):
            if str[0] == "-":
                sign = -1
            str = str[1:]

        # check for leading digit
        if not str[0].isdigit():
            return 0

        # ignore the non-digit appended behind
        # The string can contain additional characters after those that form the integral number,
        # which are ignored and have no effect on the behavior of this function
        for ind, val in enumerate(str):  # find the 1st non-digit
            if not val.isdigit():
                str = str[:ind]
                break




        # convert char array to integer
        sum = 0
        scale = 1
        for element in str[::-1]:
            sum += scale*int(element)
            scale *= 10

        # return sign*sum, and pay attention to the C constraints
        result = sign*sum
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result
