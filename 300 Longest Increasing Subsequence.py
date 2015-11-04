"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one
LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
__author__ = 'Daniel'


class Solution(object):
    def lengthOfLIS(self, A):
        """
        M: min of index last value of LIS of a particular length
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        M = [-1 for _ in xrange(n+1)]
        l = 1
        M[l] = 0
        for i in xrange(1,n):
            if A[i] > A[M[l]]:
                l += 1
                M[l] = i
            else:
                j = self.bin_search(M, A, A[i], 1, l+1)
                M[j] = i

        return l

    def bin_search(self, M, A, t, lo=0, hi=None):
        if not hi: hi = len(M)
        while lo < hi:
            m = (lo+hi)/2
            if A[M[m]] == t:
                return m
            elif A[M[m]] < t:
                lo = m + 1
            else:
                hi = m

        return lo

    def lengthOfLIS_output_all(self, A):
        """
        Maintain the result of LIS
        M: min of index last value of LIS of a particular length
        R: result table, store the predecessor idx
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        M = [-1 for _ in xrange(n+1)]
        R = [-1 for _ in xrange(n)]
        l = 1
        M[l] = 0
        for i in xrange(1, n):
            if A[i] > A[M[l]]:
                l += 1
                M[l] = i
                R[i] = M[l-1]
            else:
                j = self.bin_search(M, A, A[i], 1, l+1)
                M[j] = i
                R[i] = M[j-1] if j-1 >= 1 else -1

        cur = M[l]
        ret = []
        while True:
            ret.append(A[cur])
            if R[cur] == -1: break
            cur = R[cur]

        ret = ret[::-1]
        print ret

        return l

    def lengthOfLIS_dp(self, A):
        """
        dp

        let F[i] be the LIS length ends at A[i]
        F[i] = max(F[j]+1 for all j < i if A[i] > A[j])

        avoid max() arg is an empty sequence

        O(n^2)
        :type nums: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        F = [1 for _ in xrange(n)]
        maxa = 1
        for i in xrange(1, n):
            F[i] = max(
                F[j] + 1 if A[i] > A[j] else 1
                for j in xrange(i)
            )
            maxa = max(maxa, F[i])

        return maxa


if __name__ == "__main__":
    print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])