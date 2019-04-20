#!/usr/bin/python3
"""
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
represents a binary number starting with the most significant bit.  For example,
if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary,
which is 13.

For all leaves in the tree, consider the numbers represented by the path from
the root to that leaf.

Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
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
        self.lst = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        """
        Brute force, keep a lst, space O(log n)
        Error-prone
        """
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        if not node:
            return

        self.lst.append(node.val)  # error prone
        if not node.left and not node.right:
            # leaf
            cur = 0
            for a in self.lst:
                cur <<= 1
                cur += a
            self.ret += cur
        else:
            self.dfs(node.left)
            self.dfs(node.right)
        self.lst.pop()
