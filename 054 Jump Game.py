"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
__author__ = 'Danyang'
class Solution:
    def canJump_TLE(self, A):
        """
        dp with data structure.
        complicated

        Time Limit Exceeded

        :param A: a list of integers
        :return: a boolean
        """
        length = len(A)
        dp = [set([index]) for index in range(length)]

        for ind, val in enumerate(A):
            if ind!=0 and len(dp[ind])<2:
                continue

            # jump forward
            for i in xrange(ind+1, ind+val+1):
                if i>=length:
                    break
                for item in dp[ind]:
                    dp[i].add(item)

        return 0 in dp[-1]

    def canJump_TLE2(self, A):
        """
        Simplified
        forward dp to fill True value if can jump

        O(N^2)

        Time Limit Exceeds
        :param A:
        :return:
        """
        l = len(A)
        dp = [False for _ in xrange(l+1)]  # last one is dummy
        dp[0] = True
        for ind, val in enumerate(A):
            if dp[ind]:
                for i in xrange(1, val+1):  # now jumping
                    if ind+i<l+1:
                        dp[ind+i] = True
                    else:
                        break
        return dp[-1]

    def canJump(self, A):
        """
        dp

        dp[i] represents at index i from which the max index (absolute position) it can reach
        dp[i] = max(dp[i-1], A[i]+i)
        path not recorded, information loss, but sufficient for this question
        scanning

        O(N)
        :param A: a list of integers
        :return: a boolean
        """
        l = len(A)
        # trivial
        if l<=1:
            return True

        # dp = [-1]*(l-1)  # normally starting from \phi
        dp = [-1 for _ in xrange(l)]  # no need dummy here

        dp[0] = A[0]+0  # reachable index (absolute index)
        for i in xrange(1, l):
            # check terminal condition first
            # able to reach the end index
            if dp[i-1]>=l-1:  # directly reach the end
                return True

            # fail to reach current index
            if dp[i-1]<i:
                return False

            # transition function
            dp[i] = max(dp[i-1], A[i]+i)  # PoP - Principle of Optimality

        return False



if __name__=="__main__":
    assert Solution().canJump([2, 3, 1, 1, 4])==True
    assert Solution().canJump([3, 2, 1, 0, 4])==False
