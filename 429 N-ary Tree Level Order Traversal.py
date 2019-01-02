#!/usr/bin/python3
"""
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        """
        BFS
        
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = [root]
        ret = []
        while q:
            cur = []
            q_new = []
            for e in q:
                q_new.extend(e.children)
                cur.append(e.val)

            ret.append(cur)
            q = q_new

        return ret
