"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
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
        if not root: return depth
        elif root.right and not root.left: return self.fathom(root.right, depth+1)
        elif root.left and not root.right: return self.fathom(root.left, depth+1)
        else: return min(self.fathom(root.left, depth+1),
                         self.fathom(root.right, depth+1))