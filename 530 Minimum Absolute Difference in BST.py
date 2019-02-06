#!/usr/bin/python3
"""
Given a binary search tree with non-negative values, find the minimum absolute
difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).


Note: There are at least two nodes in this BST.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: 'TreeNode') -> int:
        """
        For every node, find min and max in left or right substree.
        O(n lgn)

        To optimize:
        recursively pass the min and max, O(n)
        """
        ret = [float('inf')]  # keep reference
        self.dfs(root, ret)
        return ret[0]

    def dfs(self, node, ret):
        if not node:
            return None, None
        left_min, left_max = self.dfs(node.left, ret)
        right_min, right_max = self.dfs(node.right, ret)
        if left_max:
            ret[0] = min(ret[0], abs(node.val - left_max))
        if right_min:
            ret[0] = min(ret[0], abs(node.val - right_min))
        left_min = left_min or node.val
        right_max = right_max or node.val
        return left_min, right_max
