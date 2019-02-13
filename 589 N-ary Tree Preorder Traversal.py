#!/usr/bin/python3
"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        """
        reversely add the children to stk
        """
        ret = []
        if not root:
            return ret

        stk = [root]
        while stk:
            cur = stk.pop()
            ret.append(cur.val)
            for c in reversed(cur.children):
                stk.append(c)

        return ret
