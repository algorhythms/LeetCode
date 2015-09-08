"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the
difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
"""
from collections import OrderedDict

__author__ = 'Daniel'


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        Two Intervals k & t:
        * Use OrderedDict to remember the index and n/t to shrink the interval to -1, 0, 1.
        * In terms of index difference, since there are i-k and i+k, when scanning from left to right, only consider i-k.

        Alternative algorithms:
        Window + TreeSet (Java) / SortedSet (C++)  # TODO

        :type nums: list[int]
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False

        if t == 0:
            return self.containsNearByDuplicate(nums, k)

        od = OrderedDict()  # keep the window
        for n in nums:
            key = n/t
            for j in (-1, 0, 1):  # (n-t, n, n+t), shrink the interval
                m = od.get(key+j)
                if m is not None and abs(m-n) <= t:  # need to recheck, consider case {1, 7}, t=4
                    return True

            while len(od) >= k:
                od.popitem(False)  # not last, i.e. the first

            od[key] = n

        return False

    def containsNearByDuplicate(self, nums, k):
        od = OrderedDict()
        for n in nums:
            if od.get(n):
                return True

            while len(od) >= k:
                od.popitem(False)

            od[n] = n

        return False


if __name__ == "__main__":
    print Solution().containsNearbyAlmostDuplicate([-3, 3], 2, 4)