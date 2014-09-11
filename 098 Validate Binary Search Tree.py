"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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



