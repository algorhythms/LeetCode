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
    def isSymmetric(self, root):
        # Trivial
        if not root:
            return True

        return self.isSymmetrical(root.left, root.right)



    def isSymmetrical(self, left, right):
        # Trivial
        if not left and not right:
            return True

        # recursive
        try:
            if left.val==right.val and self.isSymmetrical(left.left, right.right) and self.isSymmetrical(left.right, right.left):
                return True
        except AttributeError:
            return False

        return False
