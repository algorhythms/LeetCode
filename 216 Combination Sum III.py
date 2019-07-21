"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""
__author__ = 'Daniel'


class Solution:
    def combinationSum3(self, k, n):
        """
        Backtracking

        :type k: int
        :type n: int
        :rtype: list[list[int]]
        """
        ret = []
        self.dfs(k, n, [], ret)
        return ret

    def dfs(self, remain_k, remain_n, cur, ret):
        if remain_k == 0 and remain_n == 0:
            ret.append(list(cur))
            return

        # check max and min reach
        if remain_k * 9 < remain_n or remain_k * 1 > remain_n:
            return

        start = 1
        if cur:
            start = cur[-1] + 1  # unique
        for i in xrange(start, 10):
            cur.append(i)
            self.dfs(remain_k - 1, remain_n - i, cur, ret)
            cur.pop()


if __name__ == "__main__":
    assert Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
