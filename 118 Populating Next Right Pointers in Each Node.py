"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children
).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        """
        bfs
        :param root: TreeNode
        :return: nothing
        """
        if not root:
            return None

        q = [root]
        while q:
            current_level = q
            q = []
            for ind, val in enumerate(current_level):
                if val.left: q.append(val.left)
                if val.right: q.append(val.right)
                try:
                    val.next = current_level[ind+1]
                except IndexError:
                    val.next = None


