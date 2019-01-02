#!/usr/bin/python3
"""
Given a non-empty array of integers, return the third maximum number in this
array. If it does not exist, return the maximum number. The time complexity
must be in O(n).
"""
__author__ = 'Danyang'
import heapq


class Solution:
    def thirdMax(self, nums):
        """
        It is an easy question but error prone:
          1. Choice of min heap or max heap: use min heap (not max heap) because
          we want to know the smallest maximum number
          2. Duplicate number
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None

        h = []
        for e in set(nums):
            if len(h) < 3:
                heapq.heappush(h, e)
            elif len(h) == 3 and e > h[0]:
                heapq.heappushpop(h, e)

        assert len(h) <= 3
        if len(h) == 3:
            ret = min(h)
        else:
            ret = max(h)
        return ret


if __name__ == "__main__":
    assert Solution().thirdMax([1, 2, 3, 4]) == 2
    assert Solution().thirdMax([4, 3, 2, 1]) == 2
    assert Solution().thirdMax([2, 2, 3, 1]) == 1
    assert Solution().thirdMax([4, 3]) == 4
