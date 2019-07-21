#!/usr/bin/python3
"""
Given a collection of candidate numbers (candidates) and a target number
(target), find all unique combinations in candidates where the candidate numbers
sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        self.dfs(candidates, 0, [], 0, target, ret)
        return ret

    def dfs(self, candidates, i, cur, cur_sum, target, ret):
        if cur_sum == target:
            ret.append(list(cur))
            return

        if cur_sum > target or i >= len(candidates):
            return

        # not choose A_i
        # to de-dup, need to jump
        j = i + 1
        while j < len(candidates) and candidates[j] == candidates[i]:
            j += 1

        self.dfs(candidates, j, cur, cur_sum, target, ret)

        # choose A_i
        cur.append(candidates[i])
        cur_sum += candidates[i]
        self.dfs(candidates, i + 1, cur, cur_sum, target, ret)
        cur.pop()
        cur_sum -= candidates[i]


if __name__ == "__main__":
    assert Solution().combinationSum2([2,5,2,1,2], 5) == [[5], [1,2,2]]
