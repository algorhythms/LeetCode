"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 10^5
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        To find the root: middle point of the array 
        To construct balance binary search tree: recurisively 
        """
        self.A = []
        self.to_array(root)
        return self.balance(self.A, 0, len(self.A))
    
    def to_array(self, node):
        if not node:
            return 

        self.to_array(node.left)
        self.A.append(node.val)
        self.to_array(node.right)

    def balance(self, A, lo, hi):
        # [lo, hi)
        if lo >= hi:
            return None

        mid = (lo + hi) // 2
        left = self.balance(A, lo, mid)
        right = self.balance(A, mid+1, hi)
        node = TreeNode(A[mid], left, right)
        return node    