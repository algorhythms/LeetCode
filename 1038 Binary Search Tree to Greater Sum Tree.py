#!/usr/bin/python3
"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
Example 2:

Input: root = [0,null,1]
Output: [1,null,1]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val <= 100
All the values in the tree are unique.
"""


class Solution:
    def __init__(self):
        self.accu = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        sum the right subtree 
        BST: to print in order (asc), in-order traversal 
        to sum greater keys: mirroed in-order traversal

        Build a sample sum tree to find pattern
        """
        self.update_and_sum(root)
        return root

    def update_and_sum(self, cur):
        if cur is None:
            return

        self.update_and_sum(cur.right)
        cur.val += self.accu
        self.accu = cur.val 
        self.update_and_sum(cur.left)