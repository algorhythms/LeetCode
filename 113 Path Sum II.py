"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :param root: TreeNode
        :param sum: integer
        :return: a list of lists of integers
        """
        result = []
        self.accumulatePathSum(root, sum, [], result)
        return result

    def accumulatePathSum(self, root, sum, cur_path, result):
        """
        DFS
        Similar to previous path sum
        """
        # trivial
        if not root:
            return

        sum = sum - root.val
        cur_path.append(root.val)
        # terminal condition
        if sum==0 and root.left is None and root.right is None:
            result.append(list(cur_path))  # new copy
            return

        # dfs with pre-checking
        if root.left: self.accumulatePathSum(root.left, sum, list(cur_path), result)  # new copy
        if root.right: self.accumulatePathSum(root.right, sum, list(cur_path), result)  # new copy
