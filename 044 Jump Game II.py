"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last
index.)
"""
__author__ = 'Danyang'
class Solution:
    def jump_TLE(self, A):
        """
        bfs
        :param A: a list of integers
        :return: integer, minimum number of jumps
        """
        if not A:
            return 0

        length = len(A)
        counter = 0
        dp = [[] for _ in A]

        q = []
        q.append(0)
        while q:
            current_level = q
            q = []
            for ind in current_level:
                if ind>=length-1:
                    return counter
                for j in xrange(ind+1, ind+A[ind]+1):
                    if j not in current_level:  # avoid duplicate
                        q.append(j)
            counter += 1
        return counter

    def jump(self, A):
        """
        Simplified bfs, use pointers to scan the array.
        Algorithm: Two Pointers

        gmax, record the max reachable index (absolute position) from the sliding window
        :param A: a list of integers
        :return: integer, minimum number of jumps
        """
        length = len(A)
        counter = 0

        start = 0
        end = 1  # max reach [0, 1)
        gmax = 0
        while end<length:  # when end==length, it has already reached the last item
            if not start<end: return 0  # avoid dead loop
            for i in xrange(start, end):
                gmax = max(gmax, A[i]+i)

            counter += 1
            start = end
            end = gmax+1

        return counter


if __name__=="__main__":
    print Solution().jump([3, 2, 1, 0, 4])
    assert Solution().jump([2,3,1,1,4])==2
