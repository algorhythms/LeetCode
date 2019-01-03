#!/usr/bin/python3
"""
Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is incrementing n - 1
elements by 1.
"""


class Solution:
    def minMoves(self, nums):
        """
        List out, find the pattern
        for every operation, the max number does not change, then bring the min
        number 1 step closer to the max.

        :type nums: List[int]
        :rtype: int
        """
        mini = min(nums)
        return sum(map(lambda e: e - mini, nums))


if __name__ == "__main__":
    assert Solution().minMoves([1, 2, 3]) == 3
