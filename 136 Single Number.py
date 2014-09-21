"""
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""
__author__ = 'Danyang'
class Solution:
    def singleNumber(self, A):
        """
        Cannot use hash table since extra memory
        Use XOR instead

        Algorithm:
        Concept of RAID
        XOR
        bits:
        consider a list of 4-bit number:
        0000
        0001
        0010
        ...
        1111

        appear twice:
        num^num is 0
        storage ^= (num^num) is storage ^= 0, which is storage itself

        if only appear once:
        storage ^= num is the num, since the storage is 0 initially
        :param A: a list of integer
        :return: int
        """
        storage = 0
        for element in A:
            storage ^= element # XOR

        return storage
