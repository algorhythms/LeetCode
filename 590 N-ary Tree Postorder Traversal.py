#!/usr/bin/python3
"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its postorder traversal as: [5,6,3,2,4,1].

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


from typing import List
from collections import deque


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        maintain a stack, pop and reverse
        """
        if not root:
            return []

        ret = deque()
        stk = [root]
        visited = set()
        while stk:
            cur = stk.pop()
            ret.appendleft(cur.val)
            for c in cur.children:
                stk.append(c)

        return list(ret)
        
    def postorder_visited(self, root: 'Node') -> List[int]:
        """
        maintain a stack, if visited before, then pop
        """
        ret = []
        if not root:
            return ret

        stk = [root]
        visited = set()
        while stk:
            cur = stk[-1]
            if cur in visited:
                stk.pop()
                ret.append(cur.val)
            else:
                visited.add(cur)
                for c in reversed(cur.children):
                    stk.append(c)

        return ret
