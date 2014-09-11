"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""
__author__ = 'Danyang'
class Solution:
    def spiralOrder(self, matrix):
        """
              top
               |
        left --+-- right
               |
             bottom

        be careful with the index

        :param matrix: a list of lists of integers
        :return: a list of integers
        """
        if not matrix or not matrix[0]:
            return matrix

        result = []

        left = 0
        right = len(matrix[0])-1
        top = 0
        bottom = len(matrix)-1

        while left<=right and top<=bottom:
            for i in xrange(left, right+1):
                result.append(matrix[top][i])
            for i in xrange(top+1, bottom+1):
                result.append(matrix[i][right])
            for i in reversed(xrange(left+1, right)):
                if top<bottom:  # avoid double scanning the first row
                    result.append(matrix[bottom][i])
            for i in reversed(xrange(top+1, bottom+1)):
                if left<right:  # avoid double scanning the first column
                    result.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result

if __name__=="__main__":
    print Solution().spiralOrder([[2, 3]])