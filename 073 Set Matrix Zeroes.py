"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
__author__ = 'Danyang'
class Solution:
    def setZeroes_error(self, matrix):
        """
        store the zero at the head

        constant space, O(2)
        :param matrix: a list of lists of integers
        :return: NOTHING, MODIFY matrix IN PLACE.
        """
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        for row in xrange(m):
            for col in xrange(n):
                if matrix[row][col]==0:
                    matrix[0][col]=0  # previously scanned, safe to modify
                    matrix[row][0]=0  # previously scanned, safe to modify

        for row in xrange(m):
            if matrix[row][0]==0:
                for col in xrange(n):
                    matrix[row][col] = 0

        for col in xrange(n):
            if matrix[0][col]==0:
                for row in xrange(m):
                    matrix[row][col] = 0


    def setZeroes(self, matrix):
        """
        store the zero at the head
        constant space
        :param matrix: a list of lists of integers
        :return: NOTHING, MODIFY matrix IN PLACE.
        """
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        # special treatment for row and col 
        clear_first_row = False
        clear_first_col = False
        for row in xrange(m):
            if matrix[row][0]==0:
                clear_first_col = True
        for col in xrange(n):
            if matrix[0][col]==0:
                clear_first_row = True

        for row in xrange(1, m):
            for col in xrange(1, n):
                if matrix[row][col]==0:
                    matrix[0][col] = 0  # previously scanned, safe to modify
                    matrix[row][0] = 0  # previously scanned, safe to modify

        for row in xrange(1, m):  # avoid 0 at (0, 0) affect the entire matrix
            if matrix[row][0]==0:
                for col in xrange(n):
                    matrix[row][col] = 0

        for col in xrange(1, n):  # avoid 0 at (0, 0) affect the entire matrix
            if matrix[0][col]==0:
                for row in xrange(m):
                    matrix[row][col] = 0

        if clear_first_row:
            for col in xrange(n):
                matrix[0][col] = 0
        if clear_first_col:
            for row in xrange(m):
                matrix[row][0] = 0



