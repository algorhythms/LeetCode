"""
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
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
        self.get_max_component(root)
        # global_max can in ANY path in the tree
        return self.global_max

    def get_max_component(self, root):
        """
        Algorithm:
        dfs
        The path may start and end at any node in the tree.

           parent
           /
          cur
         /  \
         L  R

        at current: the candidate max (final result) is cur+L+R
        at current: the max component (intermediate result) is cur or cur+L or cur+R

        Reference: http://fisherlei.blogspot.sg/2013/01/leetcode-binary-tree-maximum-path-sum.html

        :param root:
        :return:
        """
        if not root:
            return 0

        left_max_component = self.get_max_component(root.left)
        right_max_component = self.get_max_component(root.right)

        # update global max
        current_max_sum = max(root.val, root.val+left_max_component, root.val+right_max_component, root.val+left_max_component+right_max_component)  # four situations
        self.global_max = max(self.global_max, current_max_sum)

        # return value for upper layer to calculate the current_max_sum
        return max(root.val, root.val+left_max_component, root.val+right_max_component)  # excluding arch (i.e. root.val+left_max_component+right_max_component)




