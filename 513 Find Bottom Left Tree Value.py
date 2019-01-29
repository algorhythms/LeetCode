#!/usr/bin/python3
"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        BFS

        :type root: TreeNode
        :rtype: int
        """
        q = [root]
        while q:
            ret = q[0].val
            cur_q = []
            for e in q:
                if e.left:
                    cur_q.append(e.left)
                if e.right:
                    cur_q.append(e.right)
            q = cur_q

        return ret
