"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/
deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this
string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to
follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should
be stateless.
"""
from collections import deque

__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """
        bfs
        Encodes a tree to a single string.

        encode to: 1, 2, 3, null, null, 4, 5, null, null, null, null
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"

        ret = []
        q = []
        q.append(root)
        ret.append(str(root.val))  # add result when enqueue
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                if cur.left: q.append(cur.left)
                ret.append(self.encode(cur.left))
                if cur.right: q.append(cur.right)
                ret.append(self.encode(cur.right))

            q = q[l:]

        return ",".join(ret)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        decode: 1, 2, 3, null, null, 4, 5, null, null, null, null
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(",")
        root = self.decode(lst[0])

        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()
            if i < len(lst):
                cur.left = self.decode(lst[i])
                i += 1
                if cur.left: q.append(cur.left)
            if i < len(lst):
                cur.right = self.decode(lst[i])
                i += 1
                if cur.right: q.append(cur.right)

        return root

    def decode(self, s):
        if s == "null":
            return None
        else:
            return TreeNode(int(s))

    def encode(self, node):
        if not node:
            return "null"
        else:
            return str(node.val)
