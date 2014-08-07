__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        """
        DFS
        """
        # trivial
        if not root:
            return False

        sum = sum-root.val

        # terminal condition
        if sum==0 and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)




