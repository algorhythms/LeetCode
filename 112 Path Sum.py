"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        dfs

        :param root: TreeNode
        :param sum: int
        :return: boolean
        """
        # trivial
        if not root:
            return False

        # don't prune, possible negative
        # if sum<0:
        #    return False

        sum = sum-root.val

        # terminal condition
        if sum==0 and root.left is None and root.right is None:
            return True

        # dfs without pre-checking
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)




