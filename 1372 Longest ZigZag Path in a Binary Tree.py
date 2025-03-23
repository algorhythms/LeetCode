"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

 

Example 1:


Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).
Example 2:


Input: root = [1,1,1,null,1,null,null,1,1,null,1]
Output: 4
Explanation: Longest ZigZag path in blue nodes (left -> right -> left -> right).
Example 3:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 5 * 10^4].
1 <= Node.val <= 100
"""
import functools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionN2:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Brute force visit every node, choose left or right, O(N^2)

        Memoization: O(N)
        """
        self.maxa = 0
        self.visit(root)
        return self.maxa

    @functools.lru_cache(maxsize=None)
    def dfs(self, node, is_left) -> int:
        if not node:
            return 0
        
        if is_left:
            l = self.dfs(node.right, False)
        else:
            l = self.dfs(node.left, True)
        
        ret = l + 1
        self.maxa = max(self.maxa, ret-1)
        return ret 

    def visit(self, node):
        if not node:
            return 
        
        self.dfs(node, True)
        self.dfs(node, False)
        self.visit(node.left)
        self.visit(node.right)


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxa = 0
        self.dfs(root, True, 0)
        self.dfs(root, False, 0)  # redundant
        return self.maxa - 1

    def dfs(self, node, is_left, l):
        if not node:
            return

        l += 1
        self.maxa = max(self.maxa, l)
        
        if is_left:
            self.dfs(node.right, False, l)
            # restart from node
            self.dfs(node.left, True, 1)
        else:
            self.dfs(node.left, True, l)
            # restart from node
            self.dfs(node.right, False, 1)