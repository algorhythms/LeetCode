#!/usr/bin/python3
"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go
downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000
to 1,000,000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: TreeNode, target: int) -> int:
        """
        The path does not need to start or end at the root or a leaf, but it
        must go downwards (traveling only from parent nodes to child nodes).

        Downward path
        """
        self.dfs(root, target, 0, defaultdict(int))
        return self.count

    def dfs(self, node, target, cur_sum, prefix_sum_counter):
        if not node:
            return

        cur_sum += node.val
        # delta = target - cur_sum  # error
        delta = cur_sum - target
        self.count += prefix_sum_counter[delta]
        if delta == 0:
            self.count += 1

        prefix_sum_counter[cur_sum] += 1
        self.dfs(node.left, target, cur_sum, prefix_sum_counter)
        self.dfs(node.right, target, cur_sum, prefix_sum_counter)
        prefix_sum_counter[cur_sum] -= 1
        

class SolutionComplex:
    def pathSum(self, root, sum):
        """
        Brute force: two dfs, O(n^2)

        Prefix sum in Tree, starting from root - O(n)
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        count = [0]  # pass as a reference
        self.dfs(root, sum, 0, {}, count)
        return count[0]

    def dfs(self, root, sum, cur_sum, prefix_sum, count):
        """
        Root to node sum
        prefix_sum: Dict[int, int], sum -> count
        """
        if not root:
            return

        cur_sum += root.val
        # ∃ prefix_sum: cur_sum - prefix_sum = sum
        diff = cur_sum - sum
        if diff in prefix_sum:
            count[0] += prefix_sum[diff]
        if diff == 0:  # trivial case
            count[0] += 1

        prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        self.dfs(root.left, sum, cur_sum, prefix_sum, count)
        self.dfs(root.right, sum, cur_sum, prefix_sum, count)
        prefix_sum[cur_sum] -= 1  # pop to save space
