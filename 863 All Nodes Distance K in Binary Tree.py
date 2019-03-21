#!/usr/bin/python3
"""
We are given a binary tree (with root node root), a target node, and an integer
value K.

Return a list of the values of all nodes that have a distance K from the target
node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        similar to SolutionComplicated
        get its ancestor's distance, but at the same down go down through the tree

        O(N), vist each node 2 times
        """
        ret = []
        self.ancestor_dist(root, K, target, ret)
        return ret

    def dfs_down(self, node, d, ret):
        """
        same as dfs1
        """
        if not node:
            return
        if d == 0:
            ret.append(node.val)
        else:
            self.dfs_down(node.left, d - 1, ret)
            self.dfs_down(node.right, d - 1, ret)

    def ancestor_dist(self, node, K, target, ret):
        if not node:
            return float('inf')

        if node.val == target.val:
            # d = 0
            self.dfs_down(node, K, ret)
            return 0
        else:
            l = self.ancestor_dist(node.left, K, target, ret)
            r = self.ancestor_dist(node.right, K, target, ret)
            d = min(l, r) + 1
            if d == K:
                ret.append(node.val)
            elif l == float('inf'):
                self.dfs_down(node.left, K - d - 1, ret)
            else:  # r == float('inf')
                self.dfs_down(node.right, K - d - 1, ret)
            return d


class SolutionComplicated:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        """
        break the problem into two part
        1st problem: target's subtree - easy to solve
        2nd problem:  mark parent, ancestor path length
        """
        ret = []
        self.dfs1(target, K, ret)
        hm = {}
        self.ancestor_dist(root, target, hm)
        self.dfs2(root, target, K, float("inf"), hm, ret)
        return ret

    def dfs1(self, node, K, ret):
        """1st problem"""
        if not node:
            return

        if K == 0:
            ret.append(node.val)
        else:
            self.dfs1(node.left, K-1, ret)
            self.dfs1(node.right, K-1, ret)

    def ancestor_dist(self, node, target, hm):
        if not node:
            return float('inf')

        if node.val == target.val:
            hm[node.val] = 0
        else:
            left = self.ancestor_dist(node.left, target, hm)
            right = self.ancestor_dist(node.right, target, hm)
            hm[node.val] = min(left, right) + 1

        return hm[node.val]

    def dfs2(self, node, target, K, dist, hm, ret):
        """2nd problem"""
        if not node:
            return

        if node.val == target.val:
            return

        dist = min(dist, hm[node.val])
        if dist == K:
            ret.append(node.val)

        self.dfs2(node.left, target, K, dist + 1, hm, ret)
        self.dfs2(node.right, target, K, dist + 1, hm, ret)
