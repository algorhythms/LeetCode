__author__ = 'Danyang'
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        """
        Algorithms: Two Pointers, open & closed
        Data structure: array

        del, pop(), or remove() are not allowed.
        return the length of "shrunk" array
        The array remains the same length
        """

        length = len(A)

        # trivial
        if length==0 or length==1:
            return length

        # closed pointer, open pointer
        closed_ptr = 0
        open_ptr = 1
        while open_ptr<length:
            # find the next non-duplicate:
            if A[closed_ptr]==A[open_ptr]:
                open_ptr += 1
                continue

            non_duplicate = A[open_ptr]
            A[closed_ptr+1] = non_duplicate
            closed_ptr += 1

        return closed_ptr+1 # length is index+1