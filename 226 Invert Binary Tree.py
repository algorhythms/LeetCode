"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can't invert a binary tree on a whiteboard
so fuck off.
"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree_recur(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        self.invertTree_recur(root.left)
        self.invertTree_recur(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree(self, root):
        """
        iterative solution
        Dual stack algorithm
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        stk = []  # [L, R]
        post = []  # [cur, R, L]

        stk.append(root)
        cur = None
        while stk:
            cur = stk.pop()
            post.append(cur)
            if cur.left:
                stk.append(cur.left)
            if cur.right:
                stk.append(cur.right)

        while post:
            cur = post.pop()
            cur.left, cur.right = cur.right, cur.left

        return cur