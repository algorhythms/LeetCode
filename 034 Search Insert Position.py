"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""
__author__ = 'Danyang'
class Solution:
    def searchInsert_complex(self, A, target):
        """
        binary search
        iterative solution
        :param A: a list of integers
        :param target: an integer to be inserted
        :return: integer
        """
        length = len(A)
        if not A or length==0:
            return 0

        start = 0
        end = length -1
        # while start<=end:
        while True:
            mid = (start+end)/2
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                end = mid-1
                if not start<=end:
                    # return end if end>=0 else 0
                    return mid if mid>=0 else 0
            else:
                start = mid+1
                if not start<=end:
                    return start

    def searchInsert(self, A, target):
        """
        binary search
        iterative solution
        :param A: a list of integers
        :param target: an integer to be inserted
        :return: integer
        """
        length = len(A)
        if not A or length==0:
            return 0

        start = 0
        end = length
        while start<end:
            mid = (start + end) / 2
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                end = mid
            else:
                start = mid + 1

        return start

if __name__=="__main__":
    assert Solution().searchInsert([1, 3, 5, 6], 5)==2
    assert Solution().searchInsert([1, 3, 5, 6], 2)==1
    assert Solution().searchInsert([1, 3, 5, 6], 7)==4
    assert Solution().searchInsert([1, 3, 5, 6], 0)==0



