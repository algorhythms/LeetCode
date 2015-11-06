"""
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child
connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    /
   2
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

"""
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.maxa = 0

    def longestConsecutive(self, root):
        self.longest(root)
        return self.maxa

    def longest(self, root):
        """
        longest ended at root
        """
        if not root:
            return 0

        maxa = 1
        l = self.longest(root.left)
        r = self.longest(root.right)
        if root.left and root.val+1 == root.left.val:
            maxa = max(maxa, l+1)
        if root.right and root.val+1 == root.right.val:
            maxa = max(maxa, r+1)

        self.maxa = max(self.maxa, maxa)
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