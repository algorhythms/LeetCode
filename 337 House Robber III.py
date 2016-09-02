"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the
"root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that
"all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses
were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
__author__ = 'Daniel'


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.cache_rob = {}
        self.cache_notrob = {}

    def rob(self, root):
        """
        possible rob at root
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root not in self.cache_rob:
            val = max(
                self.notrob(root),
                root.val + self.notrob(root.left) + self.notrob(root.right)
            )
            self.cache_rob[root] = val

        return self.cache_rob[root]

    def notrob(self, root):
        """
        not rob at the root
        :param root: TreeNode
        :return: int
        """
        if root is None:
            return 0

        if root not in self.cache_notrob:
            val = (
                self.rob(root.left) +
                self.rob(root.right)
            )

            self.cache_notrob[root] = val

        return self.cache_notrob[root]


class SolutionTLE(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        return max(
            self.dorob(root),
            self.notrob(root)
        )

    def dorob(self, root):
        if root is None:
            return 0

        return (
            root.val +
            self.notrob(root.left) +
            self.notrob(root.right)
        )

    def notrob(self, root):
        if root is None:
            return 0

        return (max(self.notrob(root.left), self.rob(root.left)) +
                    max(self.notrob(root.right), self.rob(root.right)))
