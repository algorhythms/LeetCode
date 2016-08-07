"""
Premium Question
"""
__author__ = 'Daniel'


class Solution(object):
    def maxSubArrayLen(self, A, k):
        """
        Search problem
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        m = {0: -1}  # initial condition, sum -> idx
        maxa = 0
        s = 0
        for i in xrange(len(A)):
            s += A[i]
            t = s - k  # s - t = k
            if t in m:
                maxa = max(maxa, i - m[t])

            if s not in m:
                m[s] = i

        return maxa
