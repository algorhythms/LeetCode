"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """

        :type root: TreeNode
        :rtype: list[str]
        """
        if not root:
            return []

        ret = []
        self.dfs(root, [], ret)
        return ret

    def dfs(self, cur, path, ret):
        """
        pre-check
        """
        path.append(cur)
        if not cur.left and not cur.right:
            ret.append("->".join(map(lambda x: str(x.val), path)))
            return

        if cur.left:
            self.dfs(cur.left, path, ret)
            path.pop()  # pop the shared path

        if cur.right:
            self.dfs(cur.right, path, ret)
            path.pop()  # pop the shared path

    def dfs_path(self, cur, path, ret):
        if not cur:
            return

        path.append(cur)
        if not cur.left and not cur.right:
            ret.append("->".join(map(lambda x: str(x.val), path)))

        self.dfs_path(cur.left, path, ret)
        self.dfs_path(cur.right, path, ret)
        path.pop()
