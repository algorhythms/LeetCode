__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
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
