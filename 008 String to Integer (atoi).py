__author__ = 'Danyang'
class Solution:
    # @return an integer
    def atoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # clean
        str = str.strip()
        if not str:
            return 0

        # clean up leading sign
        sign = 1
        if str[0] in ("+", "-"):
            if str[0]=="-":
                sign = -1
            str = str[1:]

        # check for leading digit
        if not str[0].isdigit():
            return  0

        # ignore the non-digit appended behind
        # The string can contain additional characters after those that form the integral number, \
        # which are ignored and have no effect on the behavior of this function
        for ind, val in enumerate(str):
            if not val.isdigit():
                str = str[:ind]
                break




        # convert
        sum = 0
        scale = 1
        for element in str[::-1]:
            sum += scale*int(element)
            scale *= 10

        # return sign*sum
        result = sign*sum
        if result>INT_MAX:
            return INT_MAX
        if result<INT_MIN:
            return INT_MIN
        return result
