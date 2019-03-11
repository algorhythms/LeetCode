#!/usr/bin/python3
"""
Given a Binary Search Tree (BST) with the root node root, return the minimum
difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1, it occurs between node 1 and
node 2, also between node 3 and node 2.
Note:

The size of the BST will be between 2 and 100.
The BST is always valid, each node's value is an integer, and each node's value
is different.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None
        self.ret = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        """
        in-order traversal
        """
        if not root:
            return

        self.minDiffInBST(root.left)
        if self.prev:
            self.ret = min(self.ret, root.val - self.prev)
        self.prev = root.val
        self.minDiffInBST(root.right)
        return self.ret
