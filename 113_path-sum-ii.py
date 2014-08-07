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
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        cur_path = []
        lst = []
        self.accumulatePathSum(root, sum, cur_path, lst)
        return lst

    def accumulatePathSum(self, root, sum, cur_path, lst):
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
            lst.append(list(cur_path))  # new copy
            return

        self.accumulatePathSum(root.left, sum, list(cur_path), lst)  # new copy
        self.accumulatePathSum(root.right, sum, list(cur_path), lst)  # new copy
