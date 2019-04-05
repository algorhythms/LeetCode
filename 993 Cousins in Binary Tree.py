#!/usr/bin/python3
"""
In a binary tree, the root node is at depth 0, and children of each depth k node
are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have
different parents.

We are given the root of a binary tree with unique values, and the values x and
y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are
cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pi = []
        self.depths = []

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        """
        need to know parent and depth
        """
        self.dfs(None, root, x, 0)
        self.dfs(None, root, y, 0)
        if len(self.pi) != 2:
            return False
        return self.pi[0] != self.pi[1] and self.depths[0] == self.depths[1]


    def dfs(self, pi, node, x, depth):
        if not node:
            return

        if node.val == x:
            self.pi.append(pi)
            self.depths.append(depth)
            return

        self.dfs(node, node.left, x, depth + 1)
        self.dfs(node, node.right, x, depth + 1)
