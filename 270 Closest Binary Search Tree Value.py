"""
Premium Question
"""
import sys

__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        Divide the problem into 2 parts:
        1. find the value just smaller than target
        2. find the value just larger than target
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        lo = [-sys.float_info.max]
        self.find(root, target, lo, True)
        hi = [sys.float_info.max]
        self.find(root, target, hi, False)
        if hi[0] - target < target - lo[0]:
            return int(hi[0])
        else:
            return int(lo[0])

    def find(self, root, target, ret, lower=True):
        if not root:
            return

        if root.val == target:
            ret[0] = root.val
            return

        if root.val < target:
            if lower: ret[0] = max(ret[0], root.val)
            self.find(root.right, target, ret, lower)
        else:
            if not lower: ret[0] = min(ret[0], root.val)
            self.find(root.left, target, ret, lower)


if __name__ == "__main__":
    assert Solution().closestValue(TreeNode(2147483647), 0.0) == 2147483647
