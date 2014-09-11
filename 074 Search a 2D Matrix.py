"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
"""
__author__ = 'Danyang'
class Solution:
    def searchMatrix(self, matrix, target):
        """
        binary search. Two exactly the same binary search algorithm
        :param matrix: a list of lists of integers
        :param target: an integer
        :return: a boolean
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # binary search
        start = 0
        end = m  # [0, m)
        while start<end:
            mid = (start+end)/2
            if matrix[mid][0]==target:
                return True
            if target<matrix[mid][0]:
                end = mid
            elif target>matrix[mid][0]:
                start = mid+1


        lst = matrix[end] if matrix[end][0]<=target else matrix[start]  # positioning !

        # binary search
        start = 0
        end = n  # [0, n)
        while start<end:
            mid = (start+end)/2
            if lst[mid]==target:
                return True
            if target<lst[mid]:
                end = mid
            elif target>lst[mid]:
                start = mid+1

        return False

if __name__=="__main__":
    assert Solution().searchMatrix([[1], [3]], 3)==True