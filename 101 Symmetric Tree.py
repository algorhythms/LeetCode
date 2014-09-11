"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        dfs
        :param root: TreeNode
        :return: boolean
        """
        # Trivial
        if not root:
            return True

        return self.isSymmetrical(root.left, root.right)


    def isSymmetrical(self, mirror_left, mirror_right):
        # Trivial
        if not mirror_left and not mirror_right:
            return True

        # recursive
        try:
            if mirror_left.val==mirror_right.val and self.isSymmetrical(mirror_left.left, mirror_right.right) and self.isSymmetrical(mirror_left.right, mirror_right.left):
                return True
        except AttributeError:
            return False

        return False
