#!/usr/bin/python3
"""
Given a non-empty integer array, find the minimum number of moves required to
make all array elements equal, where a move is incrementing a selected element
by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one
element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""


class Solution:
    def pivot(self, A, lo, hi):
        pivot = lo
        closed = pivot  # closed == pivot, means no closed set
        for i in range(lo + 1, hi):
            if A[i] < A[pivot]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[pivot] = A[pivot], A[closed]
        return closed  # the pivot index

    def quick_select(self, nums, lo, hi, k):
        """find k-th (0-indexed)"""
        pivot = self.pivot(nums, lo, hi)
        if pivot == k:
            return nums[pivot]
        elif pivot > k:
            return self.quick_select(nums, lo, pivot, k)
        else:
            return self.quick_select(nums, pivot + 1, hi, k)


    def minMoves2(self, nums):
        """
        find the median rather than the average

        No matter which middle point you pick, the total running length for min
        and max is the same.  |-------|-----|

        So, we can effectively reduce the problem size from n to n-2 by
        discarding min and max points.
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        median = self.quick_select(nums, 0, n, n//2)
        return sum(map(lambda x: abs(x - median), nums))

    def find_median(self, nums):
        n = len(nums)
        nums.sort()
        return nums[n//2]

    def minMoves2_error(self, nums):
        """
        move to the average, since incr and decr cost is 1

        error at [1, 0, 0, 8, 6]

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        avg = round(sum(nums) / n)
        return sum(map(lambda x: abs(x - avg), nums))


if __name__ == "__main__":
    assert Solution().minMoves2([1,2,3]) == 2
    assert Solution().minMoves2([1,0,0,8,6]) == 14
