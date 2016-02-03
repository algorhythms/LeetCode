"""
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall
run time complexity should be O(log (m+n)).
"""
__author__ = 'Danyang'


class Solution:
    def findMedianSortedArrays(self, A, B):
        """
        Merge two arrays to get the median, O((m+n)/2)

        Algorithm: Find k-th element in 2 array

        A: A_left A[m/2] A_right
        B: B_left B[n/2] A_right
        if A[m/2]>B[n/2] and k>m/2+n/2, then disregard B_left and B[n/2]
        if A[m/2]>B[n/2] and k<=m/2+n/2, then disregard A_right and A[m/2]
        if A[m/2]<=B[n/2] and k>m/2+n/2, then disregard A_left and A[m/2]
        if A[m/2]<=B[n/2] and k<=m/2+n/2, then disregard B_right and B[n/2]

        whether to disregard A[m/2] or B[n/2] takes time to consider
        
        T(N) = T(3/4 N) + O(1), thus T(N) = O(lg N) where N = |A|+|B|
        O(log (m+n)), thus binary search.

        :param A: list
        :param B: list
        :return: float
        """
        m = len(A)
        n = len(B)
        if ((m+n)&1 == 0):
            return (self.find_kth(A, B, (m+n)/2)+self.find_kth(A, B, (m+n)/2-1))/2.0
        else:
            return self.find_kth(A, B, (m+n)/2)

    def find_kth(self, A, B, k):
        """

        :param A:
        :param B:
        :param k: index starting from 0
        :return:
        """
        if not A:  return B[k]
        if not B:  return A[k]
        if k == 0: return min(A[0], B[0])

        m, n = len(A), len(B)
        # pay attention to consider the equal sign. Assigning equal sign is an art.
        if A[m/2] >= B[n/2]:
            if k > m/2+n/2:
                return self.find_kth(A, B[n/2+1:], k-n/2-1)  # exclude B[n/2] to make progress
            else:
                return self.find_kth(A[:m/2], B, k)  # exclude A[m/2] to make progress
        else:
            return self.find_kth(B, A, k)


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 2], [1, 2, 3]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [3]) == 2
    assert Solution().findMedianSortedArrays([1], [2, 3]) == 2
    assert Solution().findMedianSortedArrays([1, 2], [1, 2]) == 1.5
