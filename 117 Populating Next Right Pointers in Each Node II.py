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
        same as Populating Next Right Pointers in Each Node I 
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


