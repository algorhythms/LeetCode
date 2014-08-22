__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    global_max = -1<<31
    def maxPathSum(self, root):
        """
        :param root: TreeNode
        :return: integer
        """
        self.getMax(root)
        # global_max can in ANY path in the tree
        return self.global_max

    def getMax(self, root):
        """
        dfs
        The path may start and end at any node in the tree.
        :param root:
        :return:
        """
        if not root:
            return 0

        left_max_sum = self.getMax(root.left)
        right_max_sum = self.getMax(root.right)

        # update global max
        current_max_sum = max(root.val, root.val+left_max_sum, root.val+right_max_sum, root.val+left_max_sum+right_max_sum)  # four situation
        self.global_max = max(self.global_max, current_max_sum)

        # return value for upper layer to calculate the current_max_sum 
        return max(root.val, root.val+left_max_sum, root.val+right_max_sum)  # excluding arch (i.e. root.val+left_max_sum+right_max_sum)




