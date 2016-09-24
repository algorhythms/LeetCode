"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
"""
__author__ = 'Danyang'


class Solution(object):
    def multiply(self, num1, num2):
        """
        Google Phone Interview Question, 20 Sep 2013
        Steps:
        * multiply by 1 digit at a time
        * add the temporary results up

        To make the processing easier:
        * order the two numbers
        * reverse the numbers

        Solved around 1 hour

        :param num1: String
        :param num2: String
        :return: String
        """
        result = []

        # pre processing
        if len(num1) > len(num2):  # order them first
            return self.multiply(num2, num1)

        # reverse them first
        num1 = map(int, list(num1[::-1]))
        num2 = map(int, list(num2[::-1]))

        # multiply by 1 digit at a time
        for d in num1:
            result.append(self.multiply_1_digit(d, num2))

        # add the temporary results up
        lst = self.add_list(result)

        # post processing
        lst.reverse()  # reverse back
        result = "".join(map(str, lst)).lstrip("0")
        if not result:
            return "0"
        return result

    def multiply_1_digit(self, digit, num):
        """
        :param digit: String
        :param num: String
        :return: list of digit in reverse order
        """
        ret = []

        carry = 0
        for elt in num:
            mul = elt*digit + carry
            carry = mul/10
            mul %= 10
            ret.append(mul)

        if carry != 0:
            ret.append(carry)

        return ret

    def add_list(self, lst):
        """
        add lst of string
        :param lst:
        :return:
        """
        sig = 0
        ret = [0]
        for ind, val in enumerate(lst):
            for i in xrange(sig): val.insert(0, 0)  # possible deque
            ret = self.add(ret, val)
            sig += 1
        return ret

    def add(self, num1, num2):
        """
        :param num1: list of digits in reverse order
        :param num2: list of digits in reverse order
        :return: list of digits in reverse order
        """

        if len(num1) > len(num2):
            return self.add(num2, num1)

        ret = []
        carry = 0
        for idx in xrange(len(num2)):  # longer one
            try:
                sm = num1[idx] + num2[idx] + carry
            except IndexError:
                sm = num2[idx] + carry

            carry = sm/10
            ret.append(sm % 10)

        if carry != 0:
            ret.append(carry)

        return ret


if __name__ == "__main__":
    solution = Solution()
    assert [1, 2] == solution.add([2, 1], [9])
    assert str(123*999) == solution.multiply("123", "999")
    assert str(0) == solution.multiply("0", "0")
    assert str(123*456) == solution.multiply("123", "456")
