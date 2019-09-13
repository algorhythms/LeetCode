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

             t
             __
          l |  | r
            |__|
             b

        be careful with the index: be greedy for the first scan
        [[1,2,3],
         [8,9,4],
         [7,6,5]]

        if not greedy, the middle 9 won't be scanned
        [[1,2,3],
         [8,x,4],
         [7,6,5]]

        :param matrix: a list of lists of integers
        :return: a list of integers
        """
        if not matrix or not matrix[0]:
            return matrix

        result = []

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            for c in xrange(left, right + 1):
                result.append(matrix[top][c])
            for r in xrange(top + 1, bottom + 1):
                result.append(matrix[r][right])
            for c in xrange(right - 1, left - 1, -1):
                if top < bottom:  # avoid double scanning the first row
                    result.append(matrix[bottom][c])
            for r in xrange(bottom - 1, top, -1):
                if left < right:  # avoid double scanning the first column
                    result.append(matrix[r][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result

if __name__=="__main__":
    print Solution().spiralOrder([[2, 3]])
