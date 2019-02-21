#!/usr/bin/python3
"""
Given a non-empty special binary tree consisting of nodes with the non-negative
value, where each node in this tree has exactly two or zero sub-node. If the
node has two sub-nodes, then this node's value is the smaller value among its
two sub-nodes.

Given such a binary tree, you need to output the second minimum value in the set
made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:
Input:
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ret = self.find(root)
        return -1 if ret == float('inf') else ret

    def find(self, root: TreeNode) -> int:
        """
        find the second min
        """
        if not root:
            return float('inf')

        if root.left and root.right:
            if root.left.val == root.val:
                left = self.find(root.left)
            else:
                left = root.left.val

            if root.right.val == root.val:
                right = self.find(root.right)
            else:
                right = root.right.val

            return min(left, right)

        return float('inf')
