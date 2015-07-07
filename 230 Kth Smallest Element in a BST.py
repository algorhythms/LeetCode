# -*- coding: utf-8 -*-
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:
"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = self.cnt(root.left)
        if l+1 == k:
            return root.val
        elif l+1 < k:
            return self.kthSmallest(root.right, k-(l+1))
        else:
            return self.kthSmallest(root.left, k)

    def cnt(self, root):
        if not root:
            return 0

        return 1+self.cnt(root.left)+self.cnt(root.right)