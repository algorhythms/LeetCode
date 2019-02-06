#!/usr/bin/python3
"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
key of the original BST is changed to the original key plus sum of all keys
greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        """
        in-order traversal, right first
        """
        self.walk(root, 0)
        return root

    def walk(self, node, cur_sum):
        """stateless walk"""
        if not node:
            return cur_sum
        s = self.walk(node.right, cur_sum)
        node.val += s
        return self.walk(node.left, node.val)
