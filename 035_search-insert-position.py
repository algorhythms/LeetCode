__author__ = 'Danyang'
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert_complex(self, A, target):
        """
        binary search
        iterative solution
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
        """
        length = len(A)
        if not A or length==0:
            return 0

        start = 0
        end = length - 1
        while start<=end:
            mid = (start + end) / 2
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return start

if __name__=="__main__":
    Solution().searchInsert([1, 3], 4)