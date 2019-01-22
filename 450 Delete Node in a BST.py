#!/usr/bin/python3
"""
Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Note: Time complexity should be O(height of tree).
"""

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self._delete(root, key)

    def _delete(self, root, key):
        """
        Pop the left max or right min
        Return the root to keep the parent child relationship
        """
        if not root:
            return

        # check before recursion because need to know parent
        if key < root.val:
            root.left = self._delete(root.left, key)
            return root
        elif key > root.val:
            root.right = self._delete(root.right, key)
            return root
        else:
            if root.left:
                maxa, left = self._pop_max(root.left)
                root.left = left
                root.val = maxa
                return root
            elif root.right:
                mini, right = self._pop_min(root.right)
                root.right = right
                root.val = mini
                return root
            else:
                return

    def _pop_max(self, root):
        if root.right:
            maxa, right = self._pop_max(root.right)
            root.right = right
            return maxa, root
        # irrevelant with root.left, BST property
        else:
            return root.val, root.left

    def _pop_min(self, root):
        if root.left:
            mini, left = self._pop_min(root.left)
            root.left = left
            return mini, root
        # irrevelant with root.right, BST property
        else:
            return root.val, root.right

    def _delete_error(self, root, key):
        """
        need to know the parent, keep the reference
        need to handle duplicate

        Error: need to find the max of the left subtree rather than the root
        """
        if not root:
            return

        # check before recursion because need to know parent
        if key < root.val:
            root.left = self._delete(root.left, key)
            return root
        elif key > root.val:
            root.right = self._delete(root.right, key)
            return root
        else:
            if root.left:
                root.val = root.left.val
                left = self._delete(root.left, root.left.val)
                root.left = left
                return root
            elif root.right:
                root.val = root.right.val
                right = self._delete(root.right, root.right.val)
                root.right = right
                return root
            else:
                return
