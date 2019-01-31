#!/usr/bin/python3
"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root):
        """
        BFS
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret

        q = [root]
        while q:
            ret.append(max(map(lambda e: e.val, q)))
            cur_q = []
            for e in q:
                if e.left:
                    cur_q.append(e.left)
                if e.right:
                    cur_q.append(e.right)

            q = cur_q

        return ret
