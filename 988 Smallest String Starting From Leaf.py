#!/usr/bin/python3
"""
Given the root of a binary tree, each node has a value from 0 to 25 representing
the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents
'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller: for
example, "ab" is lexicographically smaller than "aba".  A leaf of a node is a
node that has no children.)

Example 1:

Input: [0,1,2,3,4,3,4]
Output: "dba"
Example 2:

Input: [25,1,3,1,3,0,2]
Output: "adz"
Example 3:

Input: [2,2,1,null,1,0,null,0]
Output: "abc"

Note:
The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import Tuple
from collections import deque


class Solution:
    def __init__(self):
        self.mn: Tuple[int] = None

    def smallestFromLeaf(self, root: TreeNode) -> str:
        """
        dfs
        """
        self.dfs(root, deque())
        if not self.mn:
            return ""
        return "".join(
            chr(e + ord("a"))
            for e in self.mn
        )

    def dfs(self, node, cur_deque):
        if not node:
            return

        cur_deque.appendleft(node.val)
        if not node.left and not node.right:
            t = tuple(cur_deque)
            if not self.mn or t < self.mn:
                self.mn = t
        else:
            self.dfs(node.left, cur_deque)
            self.dfs(node.right, cur_deque)
        # need to pop at the end
        cur_deque.popleft()
