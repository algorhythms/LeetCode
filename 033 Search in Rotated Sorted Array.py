"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
"""
__author__ = 'Danyang'
class Solution:
    def search(self, A, target):
        """
        assume no duplicate exists in the array
        Algorithm: modification of binary search
        reference: http://fisherlei.blogspot.sg/2013/01/leetcode-search-in-rotated-sorted-array.html

        start   mid      end
        Case 1: no rotation, just normal binary search
        1, 2, 3, 4, 5, 6, 7

        Case 2: rotate a little (rotate right) (i.e. A[mid]<A[start] and A[mid]<A[end])
        7, 1, 2, 3, 4, 5, 6
        if target<A[mid]: search left
        if target>A[mid] and target<A[end]: search right
        if target>A[mid] and target>A[end]: search left

        Case 3: rotate a lot (rotate left) (i.e. A[mid]>A[start] and A[mid]>A[end])
        2, 3, 4, 5, 6, 7, 1
        if target>A[mid]: search right
        if target<A[mid] and target>A[start]: search left
        if target<A[mid] and target<A[start]: search right

        :param A: a list of integers
        :param target: an integer to be searched
        :return: index, integer
        """

        length = len(A)
        start = 0
        end = length-1  # [start, end]
        while start<=end:
            mid = (start+end)/2
            # found
            if A[mid]==target:
                return mid
            # case 1
            if A[start]<A[mid]<A[end]:
                if target>A[mid]:
                    start = mid+1
                else:
                    end = mid-1
            # case 2
            elif A[start]>A[mid] and A[mid]<A[end]:
                if target>A[mid] and target<=A[end]:
                    start = mid+1
                else:
                    end = mid -1
            # case 3
            else:
                if target<A[mid] and target>=A[start]:
                    end = mid-1
                else:
                    start = mid+1

        return -1

if __name__=="__main__":
    print Solution().search([5,1,3], 5)