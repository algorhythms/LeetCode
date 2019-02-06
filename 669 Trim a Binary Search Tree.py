#!/usr/bin/python3
"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L). You might need
to change the root of the tree, so the result should return the new root of the
trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2

  L = 1
  R = 2

Output:
    1
      \
       2
Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output:
      3
     /
   2
  /
 1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        """
        post-order traverse
        """
        return self.walk(root, L, R)

    def walk(self, node, L, R):
        if not node:
            return None

        node.left = self.walk(node.left, L, R)
        node.right = self.walk(node.right, L, R)
        if node.val < L:
            return node.right
        elif node.val > R:
            return node.left
        else:
            return node
