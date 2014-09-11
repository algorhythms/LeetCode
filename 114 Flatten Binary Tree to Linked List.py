"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """

        :param root: TreeNode
        :return: nothing, do it in place
        """
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


