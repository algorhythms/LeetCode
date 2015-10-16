"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
__author__ = 'Danyang'


class Solution(object):
    def plusOne(self, digits):
        """
        Math

        Basics of all other questions like adding, multiplying.
        :param digits: a list of integer digits
        :return: a list of integer digits
        """
        for i in xrange(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            else:
                digits[i] -= 10

        # MSB
        digits.insert(0, 1)
        return digits

    def plusOne(self, digits):
        """
        Good habit to reverse it first
        :param digits:
        :return:
        """
        digits.reverse()

        digits[0] += 1
        carry = 0
        for i in xrange(len(digits)):  # for ind, val in enumerate(digits):
            digits[i] += carry
            if digits[i] > 9:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
                break

        if carry:
            digits.append(1)

        digits.reverse()
        return digits


if __name__ == "__main__":
    digits = [9]
    assert Solution().plusOne(digits) == [1, 0]