"""
Premium Question
Recursive
Longest Consecutive Subsequence in BT
"""
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.gmax = 0

    def longestConsecutive(self, root):
        self.longest(root)
        return self.gmax

    def longest(self, cur):
        """
        longest ended at root
        Only consider increasing order
        """
        if not cur:
            return 0

        maxa = 1
        l = self.longest(cur.left)
        r = self.longest(cur.right)
        if cur.left and cur.val+1 == cur.left.val:
            maxa = max(maxa, l+1)
        if cur.right and cur.val+1 == cur.right.val:
            maxa = max(maxa, r+1)

        self.gmax = max(self.gmax, maxa)
        return maxa

    def longestConsecutive_error(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        maxa = 1
        l = self.longestConsecutive(root.left)
        r = self.longestConsecutive(root.right)
        maxa = max(maxa, l, r)
        if root.left and root.val + 1 == root.left.val:
            maxa = max(maxa, l+1)
        if root.right and root.val + 1 == root.right.val:
            maxa = max(maxa, r+1)

        return maxa