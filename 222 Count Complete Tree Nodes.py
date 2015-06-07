"""
Given a complete binary tree, count the number of nodes.

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.val)


class Solution:
    def countNodes(self, root):
        """
        O((lg n)^2)
        """
        if not root:
            return 0
        h = self.get_height(root)
        h_r = self.get_height(root.right)
        if h == h_r+1:
            return 2**(h-1)-1+1+self.countNodes(root.right)  # left_tree nodes + root + right_tree nodes
        else:
            return 2**(h-2)-1+1+self.countNodes(root.left)  # right_tree nodes + root + left_tree nodes

    def get_height(self, cur):
        h = 0  # depth starting from 0
        while cur:
            h += 1
            cur = cur.left

        return h


class Solution_TLE:
    def __init__(self):
        self.depth = 0  # depth starts from 1
        self.cnt = 0
        self.stopped = False

    def countNodes(self, root):
        """

        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.get_depth(root)
        self.fanthom(root, 1)
        return 2**(self.depth-1)-1+self.cnt

    def get_depth(self, root):
        self.depth += 1
        if root.left:
            self.get_depth(root.left)

    def fanthom(self, root, depth):
        if self.stopped:
            return

        if not root.left and not root.left:
            if self.depth == depth:
                self.cnt += 1
            else:
                self.stopped = True
            return

        if root.left:
            self.fanthom(root.left, depth+1)
        if root.right:
            self.fanthom(root.right, depth+1)

    def countNodes_TLE(self, root):
        """
        Brute Force

        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return 1+self.countNodes(root.left)+self.countNodes(root.right)


if __name__ == "__main__":
    pass
