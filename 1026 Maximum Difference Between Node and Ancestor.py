#!/usr/bin/python3
"""
Given the root of a binary tree, find the maximum value V for which there exists
different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any
child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation:
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| =
7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
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

    def maxAncestorDiff(self, root: TreeNode) -> int:
        """
        dfs return min and max
        """
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        if not node:
            return float("inf"), -float("inf")

        lmin, lmax = self.dfs(node.left)
        rmin, rmax = self.dfs(node.right)
        mini = min(lmin, rmin)
        maxa = max(lmax, rmax)
        if mini != float("inf"):
            self.ret = max(self.ret, abs(mini - node.val))
        if maxa != -float("inf"):
            self.ret = max(self.ret, abs(maxa - node.val))

        return min(mini, node.val), max(maxa, node.val)
