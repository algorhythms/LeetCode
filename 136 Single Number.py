__author__ = 'Danyang'


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        """
        Cannot use hash table since extra memory
        Use XOR instead
        """
        record = 0
        for element in A:
            record ^= element # XOR

        return record
