#!/usr/bin/python3
"""
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree.
The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.covered = {None}
        self.cnt = 0

    def minCameraCover(self, root: TreeNode) -> int:
        """
        Greedy?
        Bottom up, cover leaf's parent is strictly better than cover leaf
        """
        self.dfs(root, None)
        if root not in self.covered:
            self.covered.add(root)
            self.cnt += 1

        return self.cnt


    def dfs(self, node, pi):
        """
        post order
        rely on the parents to cover it 
        """
        if not node:
            return

        self.dfs(node.left, node)
        self.dfs(node.right, node)
        if node.left not in self.covered or node.right not in self.covered:
            self.cnt += 1
            self.covered.add(node.left)
            self.covered.add(node.right)
            self.covered.add(node)
            self.covered.add(pi)


class SolutionErrror:
    def __init__(self):
        self.covered = set()

    def minCameraCover(self, root: TreeNode) -> int:
        """
        Greedy?
        Top-down, no good.
        Bottom up, cover leaf's parent is strictly better than cover leaf
        """
        dummy = TreeNode(0)
        dummy.left = root
        self.dfs(root, dummy)
        self.covered.discard(dummy)  # swallow KeyError
        return len(self.covered)

    def dfs(self, node, pi):
        """
        post order
        """
        if not node:
            return

        self.dfs(node.left, node)
        self.dfs(node.right, node)
        # post oder
        if (
            (not node.left or node.left in self.covered) and
            (not node.right or node.right in self.covered)
        ):
            self.covered.add(pi)
            return
