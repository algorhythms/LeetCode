"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one
LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
import bisect

__author__ = 'Daniel'


class Solution(object):
    def lengthOfLIS(self, A):
        """
        MIN: min of index last value of LIS of a particular length
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        MIN = [-1 for _ in xrange(n+1)]
        k = 1
        MIN[k] = A[0]  # store value rather than index
        for v in A[1:]:
            idx = bisect.bisect_left(MIN, v, 1, k+1)
            MIN[idx] = v
            k += 1 if idx == k+1 else 0

        return k

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
        MIN: min of index last value of LIS of a particular length
        RET: result table, store the predecessor's idx (optional)
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        MIN = [-1 for _ in xrange(n+1)]
        RET = [-1 for _ in xrange(n)]
        l = 1
        MIN[l] = 0
        for i in xrange(1, n):
            if A[i] > A[MIN[l]]:
                l += 1
                MIN[l] = i

                RET[i] = MIN[l-1]  # (optional)
            else:
                j = self.bin_search(MIN, A, A[i], 1, l+1)
                MIN[j] = i

                RET[i] = MIN[j-1] if j-1 >= 1 else -1  # (optional)

        # build the LIS (optional)
        cur = MIN[l]
        ret = []
        while True:
            ret.append(A[cur])
            if RET[cur] == -1: break
            cur = RET[cur]

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
    assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4