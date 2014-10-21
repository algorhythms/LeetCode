"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :param root: TreeNode
        :return: integer
        """
        return self.fathom(root, 0)

    def fathom(self, root, depth):
        """
        DFS
        """
        if not root:
            return depth  # whether -1 or not depends on whether depth starts from 0 or 1
        if root.left is None and root.right is not None:
            return self.fathom(root.right, depth+1)
        if root.right is None and root.left is not None:
            return self.fathom(root.left, depth+1)

        return min(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))