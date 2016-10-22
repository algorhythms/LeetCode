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
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        dfs
        :param root: TreeNode
        :return: boolean
        """
        if not root:
            return True

        return self.isSymmetrical(root.left, root.right)

    def isSymmetrical(self, l, r):
        if not l and not r:
            return True

        # recursive
        if (l and r and
            l.val == r.val and self.isSymmetrical(l.left, r.right) and self.isSymmetrical(l.right, r.left)):
            return True

        return False
