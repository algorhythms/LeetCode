"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
__author__ = 'Danyang'
class Solution:
    def firstMissingPositive(self, A):
        """
        Bucket Sort without extra space
        O(n)

        Extra space is eliminated by using the array A itself as a storage

        :param A: a list of integers
        :return: an integer
        """
        if not A:
            return 1

        i = 0
        length = len(A)
        while i<length:
            current = A[i]
            if current<=0 or current>length or A[current-1]==current:  # out-of-range or in-place
                i += 1
            else:
                A[current-1], A[i] = current, A[current-1]   # go to the next iteration


        for i in xrange(length):
            if A[i]!=i+1:
                return i+1
        return A[-1]+1


if __name__=="__main__":
    assert Solution().firstMissingPositive([3,4,-1,1])==2