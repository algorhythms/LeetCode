"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.m = {
            0: None,
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

    def numberToWords(self, num):
        """
        Pay attention to the handling of 0's
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        ret = []
        self.toWords(num, ret)
        ret = filter(lambda x: x, ret)  # filter zeros
        return " ".join(map(str, ret))

    def toWords(self, num, ret):
        SIGS = [1000000000, 1000000, 1000, 100]
        for SIG in SIGS:
            num = self.partial_parse(num, SIG, ret)

        TEN = 10
        if num/TEN > 1:
            ret.append(self.m[(num/TEN)*TEN])
            ret.append(self.m[num%TEN])
        else:
            ret.append(self.m[num])

    def partial_parse(self, num, sig, ret):
        if num/sig:
            pre = []
            self.toWords(num/sig, pre)
            ret.extend(pre)
            ret.append(self.m[sig])
            num %= sig

        return num


if __name__ == "__main__":
    assert Solution().numberToWords(1234567891) == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty " \
                                                   "Seven Thousand Eight Hundred Ninety One"