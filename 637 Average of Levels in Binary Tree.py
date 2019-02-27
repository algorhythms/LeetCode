#!/usr/bin/python3
"""
Given a non-empty binary tree, return the average value of the nodes on each
level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2
is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        """
        BFS
        """
        ret = []
        if not root:
            return ret

        q = [root]
        while q:
            n = len(q)
            avg = sum(map(lambda node: node.val, q)) / n
            ret.append(avg)
            cur_q = []
            for node in q:
                if node.left:
                    cur_q.append(node.left)
                if node.right:
                    cur_q.append(node.right)

            q = cur_q

        return ret
