"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 10^4].
1 <= Node.val <= 10^4
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


MOD = int(1e9+7)
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        """
        Brute force: remove edge O(N) * calculate sum, O(N)

        cache sum O(1)
        only need to root sum, and subtree sum]

        probably only need to store root sum, not every node's sum
        """
        self.s = {}
        self.dfs(root)
        self.maxa = 0
        self.dfs_remove(root, root)
        return self.maxa % MOD

    def dfs(self, cur):
        if not cur:
            return 0
        
        s = cur.val
        s += self.dfs(cur.left)
        s += self.dfs(cur.right)
        self.s[cur] = s
        return s
    
    def dfs_remove(self, cur, root):
        if not cur:
            return 
        
        for child in [cur.left, cur.right]:
            if child:
                a = self.s[child]
                b = (self.s[root] - a)
                self.maxa = max(self.maxa, a * b)
        
        self.dfs_remove(cur.left, root)
        self.dfs_remove(cur.right, root)