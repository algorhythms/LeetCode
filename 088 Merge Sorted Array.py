__author__ = 'Danyang'
class Solution:
    def merge(self, A, m, B, n):
        """
        array, ascending order
        basic of merge sort

        CONSTANT SPACE: starting backward

        :param A: a list of integers
        :param m: an integer, length of A
        :param B: a list of integers
        :param n: an integer, length of B
        :return:
        """
        i = m-1
        j = n-1
        closed = m+n

        while i>=0 and j>=0:
            closed -= 1
            if A[i]>B[j]:
                A[closed] = A[i]
                i -= 1
            else:
                A[closed] = B[j]
                j -= 1

        # dangling
        while j>=0:
            closed -= 1
            A[closed] = B[j]
            j -= 1
