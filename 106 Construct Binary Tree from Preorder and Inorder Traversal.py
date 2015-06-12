"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        Recursive algorithm. Pre-order, in-order, post-order traversal relationship

        pre-order:  [root,         left_subtree,  right_subtree]
        in-order:   [left_subtree, root,          right_subtree]


        recursive algorithm
        :param preorder: a list of integers
        :param inorder: a list of integers
        :return: TreeNode, root
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)

        root.left = self.buildTree(preorder[1:root_index+1], inorder[0:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root
