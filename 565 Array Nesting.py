#!/usr/bin/python3
"""
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and
return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ...
} subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of
index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that
analogy, we stop adding right before a duplicate element occurs in S.



Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}


Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of A is an integer within the range [0, N-1].
"""
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        """
        You can think of it as graph. If circle, then you can start with any
        node
        """
        visited = set()
        ret = 0
        for n in nums:
            count = self.dfs(nums, n, set(), visited)
            ret = max(ret, count)

        return ret

    def dfs(self, nums, num, path, visited):
        if num in visited:
            return 0

        visited.add(num)
        path.add(num)  # path is subset of visited
        self.dfs(nums, nums[num], path, visited)
        return len(path)


if __name__ == "__main__":
    assert Solution().arrayNesting([5,4,0,3,1,6,2]) == 4
