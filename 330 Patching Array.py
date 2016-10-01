"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in
range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches
required.

Example 1:
nums = [1, 3], n = 6
Return 1.

Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:
nums = [1, 5, 10], n = 20
Return 2.
The two patches can be [2, 4].

Example 3:
nums = [1, 2, 2], n = 5
Return 0.
"""
__author__ = 'Daniel'


class Solution(object):
    def minPatches(self, nums, n):
        """
        https://discuss.leetcode.com/topic/35494/solution-explanation

        Greedy
        Let cur_max be the current max sum can be formed by [0, i) when iterating at i-th index
        if cur_max < Ai:
          we have a void gap at [cur_max + 1, Ai]
          we need to patch a cur_max in the array to maximize the all-cover reach
        else:
          cur_max += Ai

        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cnt = 0
        cur_max = 0
        i = 0
        while cur_max < n:
            if i >= len(nums) or cur_max + 1 < nums[i]:
                cur_max += cur_max + 1
                cnt += 1
            else:
                cur_max += nums[i]
                i += 1

        return cnt

    def minPatches2(self, nums, n):
        """
        https://discuss.leetcode.com/topic/35494/solution-explanation

        Greedy
        Let cur_max be the current max sum can be formed by [0, i) when iterating at i-th index
        if cur_max < Ai:
          we have a void gap at [cur_max + 1, Ai]
          we need to patch a cur_max in the array to maximize the all-cover reach
        else:
          cur_max += Ai

        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        nums = filter(lambda x: x <= n, nums)

        cnt = 0
        cur_max = 0
        for elt in nums:
            while cur_max + 1 < elt:
                cur_max += cur_max + 1
                cnt += 1

            cur_max += elt

        # after iterating all array element
        while cur_max < n:
            cur_max += cur_max + 1
            cnt += 1

        return cnt


if __name__ == "__main__":
    assert Solution().minPatches([1, 2, 2, 6, 34], 20) == 1