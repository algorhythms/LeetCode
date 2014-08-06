__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        """
        DFS
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
