#!/usr/bin/python3
"""
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most
frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to
the node's key.
The right subtree of a node contains only nodes with keys greater than or equal
to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the
implicit stack space incurred due to recursion does not count).
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        """
        In-order traversal
        O(1) space thus cannot keep a set of current modes
        need two passes - 1st pass to find the mode count, 2nd pass to find all
        modes equal to the mode count

        :type root: TreeNode
        :rtype: List[int]
        """
        ret = [[], 0]  # [results, length]
        self.find_mode(root, [None, 0], ret, False)
        self.find_mode(root, [None, 0], ret, True)
        return ret[0]

    def find_mode(self, root, prev, ret, collect):
        """
        prev: [previous_value, count]. Need to survice the call stack
        """
        if not root:
            return

        self.find_mode(root.left, prev, ret, collect)

        if prev[0] == root.val:
            prev[1] += 1
        else:
            prev[1] = 1
        prev[0] = root.val

        if not collect:
            ret[1] = max(ret[1], prev[1])
        else:
            if prev[1] == ret[1]:
                ret[0].append(root.val)

        self.find_mode(root.right, prev, ret, collect)

    def findMode_error(self, root):
        """
        counter (extra space) for any tree
        use recursion

        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        ret = [0, []]
        self.find_mode_error(root, root.val, ret)
        return ret[1]

    def find_mode_error(self, root, target, ret):
        cur = 0
        if not root:
            return cur

        if root.val == target:
            cur += 1
            cur += self.find_mode_error(root.left, root.val, ret)
            cur += self.find_mode_error(root.right, root.val, ret)
            if cur > ret[0]:
                ret[0], ret[1] = cur, [target]
            elif cur == ret[0]:
                ret[1].append(target)
        else:
            self.find_mode_error(root, root.val, ret)

        return cur
