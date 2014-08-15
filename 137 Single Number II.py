__author__ = 'Danyang'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        """
        No extra memory, thus unable to use hash table, requiring constant space solution

        GF(3) http://en.wikipedia.org/wiki/Finite_field_arithmetic
        reference: https://oj.leetcode.com/discuss/857/constant-space-solution#a2542
        """
        bit_0, bit_1, bit_2 = ~0, 0, 0
        for element in A:
            temp = bit_2
            bit_2 = (bit_1 & element) | (bit_2 & ~element)
            bit_1 = (bit_0 & element) | (bit_1 & ~element)
            bit_0 = (temp & element) | (bit_0 & ~element)
        return bit_1