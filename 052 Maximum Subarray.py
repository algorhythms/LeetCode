"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.
"""
__author__ = 'Danyang'
class Solution:
    def maxSubArray(self, A):
        """
        maximum sub-array problem.
        O(n) scanning
        :param A: a list of integers
        :return: integer
        """
        # trivial
        if not A:
            return 0

        # in case of A = [-1]
        largest = max(A)
        if largest<0:
            return largest

        max_result = -1<<31
        current_max = 0
        for i in range(len(A)):
            if current_max+A[i]>=0:
                current_max+=A[i]
            else:
                current_max = 0
            max_result = max(max_result, current_max)

        return max_result