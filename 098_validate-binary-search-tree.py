__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        Google Phone Interview Question, 20 Sep 2013
        recursive dfs

        alternative answer: convert the tree the array and judge whether it is sorted
        :param root: a tree node
        :return: boolean
        """
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False
        if not self.isValidBST(root.right):
            return False

        if root.left:
            if not self.get_largest(root.left) < root.val:
                return False
        if root.right:
            if not root.val < self.get_smallest(root.right):
                return False


        return True

    def get_largest(self, root):
        """
        possible dp
        :param root: TreeNode
        :return: integer
        """
        if not root.right:
            return root.val
        return self.get_largest(root.right)

    def get_smallest(self, root):
        """
        possible dp
        :param root: TreeNode
        :return: integer
        """
        if not root.left:
            return root.val
        return self.get_smallest(root.left)



