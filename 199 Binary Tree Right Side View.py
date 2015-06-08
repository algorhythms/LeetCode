"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        """
        Binary tree level traversal
        :type root: TreeNode
        :rtype: list[int]
        """
        cur_lvl = []
        nxt_lvl = []
        ret = []

        if root:
            cur_lvl.append(root)

        while cur_lvl:
            ret.append(cur_lvl[-1].val)
            while cur_lvl:
                cur = cur_lvl.pop(0)
                if cur.left: nxt_lvl.append(cur.left)
                if cur.right: nxt_lvl.append(cur.right)

            cur_lvl = nxt_lvl
            nxt_lvl = []

        return ret