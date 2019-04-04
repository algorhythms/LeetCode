#!/usr/bin/python3
"""
Given a binary tree with N nodes, each node has a different value from
{1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the
right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from
the root.  Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's
value, then preorder-traverse the left child, then preorder-traverse the right
child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of
the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.  You may
return the answer in any order.

If we cannot do so, then return the list [-1].

Example 1:

Input: root = [1,2], voyage = [2,1]
Output: [-1]
Example 2:

Input: root = [1,2,3], voyage = [1,3,2]
Output: [1]
Example 3:

Input: root = [1,2,3], voyage = [1,2,3]
Output: []

Note:

1 <= N <= 100
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = []
        self.i = 0  # currently scanning index of voyage

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        match the voyage
        Flip the least number of nodes? There is only one answer
        """
        self.dfs(root, voyage)
        return self.ret

    def dfs(self, node, voyage):
        if not node:
            return

        if node.val != voyage[self.i]:
            self.ret = [-1]
            return

        self.i += 1
        if node.left and node.right and node.left.val != voyage[self.i]:
            # flip left and right
            self.ret.append(node.val)
            self.dfs(node.right, voyage)
            self.dfs(node.left, voyage)
        else:
            self.dfs(node.left, voyage)
            self.dfs(node.right, voyage)
