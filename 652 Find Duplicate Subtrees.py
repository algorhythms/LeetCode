#!/usr/bin/python3
"""
Given a binary tree, return all duplicate subtrees. For each kind of duplicate
subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:

      2
     /
    4
and

    4
Therefore, you need to return above trees' root in the form of a list.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
from collections import defaultdict


class MerkleHash:
    def __init__(self):
        self.start_key = 0
        self.merkle_hash = defaultdict(self._auto_incr)  # subtree -> id

    def _auto_incr(self):
        self.start_key += 1
        return self.start_key

    def __call__(self, val):
        return self.merkle_hash[val]


class Solution:
    def __init__(self):
        self.counter = defaultdict(int)
        self.merkle_hash = MerkleHash()

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        Merkle hash based on current val, and left substree merkle and right merkle
        Assign each subtree a identity/hash
        Chain of hash can uniquely identify a subtree
        """
        ret = []
        self.walk(root, ret)
        return ret

    def walk(self, cur, ret) -> int:
        """
        return merkle hash id
        """
        if not cur:
            return self.merkle_hash(None)

        subtree_value = (cur.val, self.walk(cur.left, ret), self.walk(cur.right, ret))
        merkle_hash = self.merkle_hash(subtree_value)
        if self.counter[merkle_hash] == 1:
            ret.append(cur)

        self.counter[merkle_hash] += 1
        return merkle_hash


class Solution2:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        """
        Only need to return the root
        """
        ret = []
        self.walk(root, defaultdict(int), ret)
        return ret

    def walk(self, cur, counter, ret) -> str:
        """
        serialize the subtrees and check existence

        Needs to have a unique representation

        for the key, cannot but cur.val in the middle as not be able to
        differentiate between

           0
          /
         0

         0
          \
           0
        because you don't know which one is the root

        complexity: O(N) * O(N) (string concatenation),
        """
        if not cur:
            return "None"

        cur_key = ",".join([
            self.walk(cur.left, counter, ret),
            self.walk(cur.right, counter, ret),
            str(cur.val),
        ])
        if counter[cur_key] == 1:
            ret.append(cur)

        counter[cur_key] += 1
        return cur_key
