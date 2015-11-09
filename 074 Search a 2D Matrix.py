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


class Solution(object):
    def searchMatrix(self, mat, target):
        """
        binary search. Two exactly the same binary search algorithm
        :param mat: a list of lists of integers
        :param target: an integer
        :return: a boolean
        """
        if not mat:
            return False

        m = len(mat)
        n = len(mat[0])

        # binary search
        lo = 0
        hi = m  # [0, m)
        while lo < hi:
            mid = (lo+hi)/2
            if mat[mid][0] == target:
                return True
            elif mat[mid][0] < target:
                lo = mid+1
            else:
                hi = mid

        lst = mat[lo-1]  # <=

        # binary search
        lo = 0
        hi = n  # [0, n)
        while lo < hi:
            mid = (lo+hi)/2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                lo = mid+1
            else:
                hi = mid

        return False


if __name__ == "__main__":
    assert Solution().searchMatrix([[1], [3]], 3) == True