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
        end = m-1
        while start<=end:
            mid = (start+end)/2
            if matrix[mid][0]==target:
                return True
            if target<matrix[mid][0]:
                end = mid-1
            elif target>matrix[mid][0]:
                start = mid+1



        lst = matrix[end] if matrix[end][0]<=target else matrix[start]  # positioning !

        # binary search
        start = 0
        end = n-1
        while start<=end:
            mid = (start+end)/2
            if lst[mid]==target:
                return True
            if target<lst[mid]:
                end = mid-1
            elif target>lst[mid]:
                start = mid+1

        return False

if __name__=="__main__":
    print Solution().searchMatrix([[1], [3]], 3)