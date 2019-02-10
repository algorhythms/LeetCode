#!/usr/bin/python3
"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of
all left subtree node values and the sum of all right subtree node values. Null
node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input:
         1
       /   \
      2     3
Output: 1
Explanation:
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ret = [0]
        self.walk(root, ret)
        return ret[0]

    def walk(self, node: TreeNode, ret) -> int:
        """get the sum of the subtree and add the tilt"""
        if not node:
            return 0

        l = self.walk(node.left, ret)
        r = self.walk(node.right, ret)
        ret[0] += abs(l - r)
        return l + node.val + r
