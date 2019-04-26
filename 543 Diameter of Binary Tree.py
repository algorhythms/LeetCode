#!/usr/bin/python3
"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges
between them.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        """
        dfs, return the longest path (#nodes) ended at the subroot/current node
        """
        self.ret = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        """
        return #nodes ended at node including itself
        """
        if not node:
            return 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.ret = max(self.ret, l + 1 + r - 1)  # path length is the #nodes - 1
        return max(l, r) + 1
