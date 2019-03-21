#!/usr/bin/python3
"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.



Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:


We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.deepest = -1
        self.deepest_nodes = None
        self.ret = None

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        """
        lowest common ancestor of deepest node
        """
        self.down(root, 0)
        if len(self.deepest_nodes) == 1:
            return self.deepest_nodes.pop()

        self.count(root)
        return self.ret

    def down(self, node: TreeNode, d: int) -> None:
        if not node:
            return

        if d > self.deepest:
            self.deepest = d
            self.deepest_nodes = set([node])
        elif d == self.deepest:
            self.deepest_nodes.add(node)

        self.down(node.left, d + 1)
        self.down(node.right, d + 1)

    def count(self, node: TreeNode) -> int:
        if not node:
            return 0

        l = self.count(node.left)
        r = self.count(node.right)
        if l != 0 and r != 0 and l + r == len(self.deepest_nodes):
            self.ret = node

        count = l + r
        if node in self.deepest_nodes:
            count += 1
        return count
