__author__ = 'Danyang'


class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        """
        Algorithms: Two Pointers
        Partitioning the array into 3 parts, closed, open, back
        Data structure: array
        """

        open_ptr = 0
        back_ptr = -1
        while len(A)+back_ptr>=open_ptr:
            if A[open_ptr]==elem:
                A[open_ptr], A[back_ptr] = A[back_ptr], A[open_ptr]
                back_ptr -= 1
            else:
                open_ptr += 1

        return len(A)+back_ptr+1  # length is index+1



