"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
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
            return depth
        return max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
