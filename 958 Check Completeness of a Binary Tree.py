#!/usr/bin/python3
"""
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely
filled, and all nodes in the last level are as far left as possible. It can have
between 1 and 2h nodes inclusive at the last level h.

Example 1:

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values
{1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:

Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_depth = -float("inf")
        self.expecting_partial = False

    def isCompleteTree(self, root: TreeNode) -> bool:
        """
        Do it in one pass
        Left first dfs
        Record the max depth and expecting partial fill in the last level
        Need a special flag to tell whether expecting partial now
        """
        return self.dfs(root, 0)

    def dfs(self, node, d):
        if not node:
            # empty node (below leaf) is the key decision point
            if self.max_depth == -float("inf"):  # leftmost empty node
                self.max_depth = d - 1
                return True
            elif self.expecting_partial:
                return d == self.max_depth
            else:
                if d == self.max_depth + 1:
                    return True
                if d == self.max_depth:
                    self.expecting_partial = True
                    return True
                return False

        return self.dfs(node.left, d + 1) and self.dfs(node.right, d + 1)
