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
    def minDepth(self, root):
        return self.fathom(root, 0)

    def fathom(self, root, depth):
        """
        DFS
        """
        if not root:
            return depth
        if root.left is None and root.right is not None:
            return self.fathom(root.right, depth+1)
        if root.right is None and root.left is not None:
            return self.fathom(root.left, depth+1)

        return min(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))