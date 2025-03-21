"""
Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
-10^5 <= Node.val <= 10^5
-10^9 <= limit <= 10^9
"""
import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionError:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        """
        every path sum < limit => max(path_sums) < limit
        dfs to find the max pathsum
        """
        pi = TreeNode(val=0)
        pi.left = root
        self.dfs(pi, limit)
        return pi.left

    def dfs(self, node, limit):
        max_path_sum = 0
        if node.left:
            left_sum = self.dfs(node.left, limit)
            if left_sum < limit:
                node.left = None
            max_path_sum = max(max_path_sum, left_sum)
        if node.right:
            right_sum = self.dfs(node.right, limit)
            if right_sum < limit:
                node.right = None
            max_path_sum = max(max_path_sum, right_sum)

        return max_path_sum + node.val


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        """
        root to path intersection this node < limit 
        path_sum:
        1. root to node: [root, node]
        2. node to leaf: [node, leaf]

        every path sum < limit => max path sum < limit 
        """
        self.limit = limit
        pi = TreeNode(0)
        pi.left = root
        self.dfs(pi, 0)
        return pi.left
    
    def dfs(self, node, root_sum):
        """
        delete the node.left or node.right if insufficient 
        return the max leaf sum
        """
        if not node.left and not node.right:
            return node.val

        root_sum += node.val
        leaf_sum = -sys.maxsize-1
        if node.left:
            l = self.dfs(node.left, root_sum)
            if root_sum + l < self.limit:
                node.left = None

            leaf_sum = max(leaf_sum, l)

        if node.right:
            r = self.dfs(node.right, root_sum)
            if root_sum + r < self.limit:
                node.right = None 

            leaf_sum = max(leaf_sum, r)

        return leaf_sum + node.val