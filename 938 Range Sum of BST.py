#!/usr/bin/python3
"""
Given the root node of a binary search tree, return the sum of values of all
nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        traverse
        """
        self.dfs(root, L, R)
        return self.ret

    def dfs(self, node, L, R):
        if not node:
            return

        if L <= node.val <= R:
            self.ret += node.val
            self.dfs(node.left, L, R)
            self.dfs(node.right, L, R)

        elif node.val > R:
            self.dfs(node.left, L, R)
        else:
            self.dfs(node.right, L, R)
