#!/usr/bin/python3
"""
You are given an integer array sorted in ascending order (may contain
duplicates), you need to split them into several subsequences, where each
subsequences consist of at least 3 consecutive integers. Return whether you can
make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences :
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
"""
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        """
        Attribute a number to a existing consecutive subsequences
        future numbers depend on this number to form the subsequence can also
        attribtue to this existing subsequence

        If no existing one to attribtue, form a consecutive (l >= 3) by use the
        subsequent numbers by looking forward

        Let F[i] be the number of consecutive subsequence at A[i]
        """
        counter = defaultdict(int)
        for e in nums:
            counter[e] += 1

        F = defaultdict(int)
        for e in nums:
            if counter[e] == 0:
                continue
            counter[e] -= 1

            if F[e - 1] > 0:
                F[e - 1] -= 1
                F[e] += 1
            elif counter[e + 1] > 0 and counter[e + 2] > 0:
                F[e + 2] += 1
                counter[e + 1] -= 1
                counter[e + 2] -= 1
            else:
                return False

        return True

            
class Interval:
    def __init__(self, end, length):
        self.end = end
        self.length = length

    def __lt__(self, other):
        if self.end == other.end:
            return self.length < other.length

        return self.end < other.end

    def __repr__(self):
        return repr((self.end, self.length))


class Solution2:
    def isPossible(self, nums: List[int]) -> bool:
        """
        (length, last)
        heap sortest first
        >= 3, then drop

        split when duplicate
        """
        h = []
        for n in nums:
            while h and h[0].end + 1 < n:
                itvl = heapq.heappop(h)
                if itvl.length < 3:
                    return False

            if not h:
                heapq.heappush(h, Interval(n, 1))
            elif h[0].end + 1 == n:
                itvl = heapq.heappop(h)
                heapq.heappush(h, Interval(n, itvl.length + 1))
            else:  # n == end
                heapq.heappush(h, Interval(n, 1))


        for itvl in h:
            if itvl.length < 3:
                return False

        return True

if __name__ == "__main__":
    assert Solution().isPossible([1,2,3,3,4,5]) == True
    assert Solution().isPossible([1,2,3,3,4,4,5,5]) == True
    assert Solution().isPossible([1,2,3,4,4,5]) == False
