"""
Premium Question
"""
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        search

        If it is a general binary tree
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        find = [None]
        self.search(root, p, find)
        return find[0]

    def search(self, cur, p, find):
        if not cur:
            return

        if cur.val > p.val:
            find[0] = cur
            self.search(cur.left, p, find)
        else:
            self.search(cur.right, p, find)