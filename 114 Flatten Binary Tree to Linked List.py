__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        # trivial
        if not root:
            return

        lst = []
        self.dfs_traverse(root, lst)
        lst = lst[1:] # exclude root

        root.left = None
        cur = root
        for node in lst:
            node.left = None
            node.right = None
            cur.right = node
            cur = cur.right


    def dfs_traverse(self, root, lst):
        """
        pre_order traverse
        """
        if not root:
            return
        lst.append(root)
        self.dfs_traverse(root.left, lst)
        self.dfs_traverse(root.right, lst)


