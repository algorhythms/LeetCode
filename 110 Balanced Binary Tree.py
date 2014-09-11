"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        pre-order traversal

        :param root: TreeNode
        :return: boolean
        """
        if not root:
            return True
        if abs(self.fathom(root.left, 0)-self.fathom(root.right, 0))>1:
            return False

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False



    def fathom(self, root, depth):
        """
        DFS
        """
        if not root:
            return depth
        return max(self.fathom(root.left, depth + 1), self.fathom(root.right, depth + 1))
