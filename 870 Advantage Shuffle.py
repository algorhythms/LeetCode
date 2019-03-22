#!/usr/bin/python3
"""
Given two arrays A and B of equal size, the advantage of A with respect to B is
the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]


Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9
"""
from typing import List
from collections import defaultdict


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        """
        Gready select the smallest larger number
        Then we need sort A
        Iterate B and do a bisect on A? Hard to remove the chosen element on A
        unless using a balanced BST
        How about we sort B also?
        Like a merge sort, compare both sorted A and sorted B
        But we need to record the position of B's element since sorting break the
        position
        Keep a reverse index mapping is not enough, since duplicate in B
        then keep a list
        """
        idxes = defaultdict(list)
        for i, b in enumerate(B):
            idxes[b].append(i)

        n = len(A)
        A.sort()
        B.sort()
        ret = [None for _ in range(n)]
        not_used = []
        j = 0
        for a in A:
            if a > B[j]:
                i = idxes[B[j]].pop()
                ret[i] = a
                j += 1
            else:
                not_used.append(a)

        for i in range(n):
            if ret[i] is None:
                ret[i] = not_used.pop()

        return ret


if __name__ == "__main__":
    assert Solution().advantageCount([2,7,11,15], [1,10,4,11]) == [2,11,7,15]
