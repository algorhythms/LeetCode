"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.depth_bottom = {}

    def isBalanced(self, root):
        self.fathom(root, 0)
        return self._is_balanced(root, 0)

    def _is_balanced(self, cur, depth):
        """
        :param depth: depth from root to current node.
        """
        if not cur:
            return True

        h1 = h2 = depth
        if cur.left: h1 = self.depth_bottom[cur.left]
        if cur.right: h2 = self.depth_bottom[cur.right]

        if abs(h1 - h2) > 1:
            return False

        return all([self._is_balanced(cur.left, depth+1), self._is_balanced(cur.right, depth+1)])

    def fathom(self, root, depth):
        if not root:
            return depth-1

        ret = max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
        self.depth_bottom[root] = ret
        return ret


class SolutionSlow(object):
    def isBalanced(self, root):
        """
        pre-order traversal

        :param root: TreeNode
        :return: boolean
        """
        if not root:
            return True
        if abs(self.fathom(root.left, 0)-self.fathom(root.right, 0)) > 1:
            return False

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    def fathom(self, root, depth):
        """
        DFS
        """
        if not root:
            return depth-1  # test cases
        return max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
