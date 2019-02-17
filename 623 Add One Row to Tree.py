#!/usr/bin/python3
"""
Given the root of a binary tree, then value v and depth d, you need to add a row
of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree
nodes N in depth d-1, create two tree nodes with value v as N's left subtree
root and right subtree root. And N's original left subtree should be the left
subtree of the new left subtree root, its original right subtree should be the
right subtree of the new right subtree root. If depth d is 1 that means there is
no depth d-1 at all, then create a tree node with value v as the new root of the
whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        return self.add(root, v, d, 1, "left")

    def add(self, node, v, d, cur_d, child) -> TreeNode:
        # use the return value for parent's reference 
        if cur_d == d:
            new = TreeNode(v)
            setattr(new, child, node)
            return new

        if node:
            node.left = self.add(node.left, v, d, cur_d + 1, "left")
            node.right = self.add(node.right, v, d, cur_d + 1, "right")
            return node


class Solution2:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        self.add(self, root, v, d, 1)
        return root

    def add(self, node, v, d, cur_d) -> None:
        if not node:
            return

        if cur_d + 1 == d:
            left = node.left
            right = node.right
            node.left = TreeNode(v)
            node.left.left = left
            node.right = TreeNode(v)
            node.right.right = right

        self.add(node.left, v, d, cur_d + 1)
        self.add(node.right, v, d, cur_d + 1)
