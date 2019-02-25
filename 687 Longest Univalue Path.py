#!/usr/bin/python3
"""
Given a binary tree, find the length of the longest path where each node in the
path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges
between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the
tree is not more than 1000.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.find(root)
        return self.ret

    def find(self, node):
        """
        the longest path ended at node
        """
        if not node:
            return 0

        left = self.find(node.left)
        right = self.find(node.right)
        left_path = left + 1 if node.left and node.left.val == node.val else 0
        right_path = right + 1 if node.right and node.right.val == node.val else 0
        self.ret = max(self.ret, left_path + right_path)
        return max(left_path, right_path)


class Solution_error:
    def __init__(self):
        self.ret = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.find(root)
        return self.ret

    def find(self, node):
        """
        the longest path ended at node
        """
        if not node:
            return 0

        left = self.find(node.left)
        right = self.find(node.right)
        cur = 1  # node.val
        path = 1
        if left and node.left.val == node.val:
            path += left
            cur = left + 1

        if right and node.right.val == node.val:
            path += right
            if right > left:
                cur = right + 1

        self.ret = max(self.ret, path - 1)
        return cur
