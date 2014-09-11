"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        dfs
        :param p: TreeNode
        :param q: TreeNode
        :return: boolean
        """

        # trivial
        if not p and not q:
            return True

        # dfs
        try:
            if p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        except AttributeError:
            return False

        return False
