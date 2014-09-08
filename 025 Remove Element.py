"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
__author__ = 'Danyang'
class Solution:
    def removeElement(self, A, elem):
        """
        Constant space
        Algorithms: Two Pointers
        Partitioning the array into 3 parts, closed, open, back
        Data structure: array
        :param A: list
        :param elem: integer
        :return: "shrunk" list
        """

        open_ptr = 0
        back_ptr = -1  # Python style backward
        while len(A)+back_ptr>=open_ptr:
            if A[open_ptr]==elem:
                A[open_ptr], A[back_ptr] = A[back_ptr], A[open_ptr]
                back_ptr -= 1
            else:
                open_ptr += 1

        return len(A)+back_ptr+1  # length is index+1



