"""
Premium Question
"""

__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.cnt = 0

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.is_unival(root)
        return self.cnt

    def is_unival(self, cur):
        if not cur:
            return True

        is_left = self.is_unival(cur.left)
        is_right = self.is_unival(cur.right)  # attention to test condition shortcut
        if (not is_left or not is_right or
                    cur.left and cur.left.val != cur.val or
                    cur.right and cur.right.val != cur.val):
            return False
        else:
            self.cnt += 1  # for currently visiting node as the root of subtree.
            return True
