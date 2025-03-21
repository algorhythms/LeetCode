"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        after deletion, children become new tree
        """
        pi = TreeNode()
        pi.left = root
        acc = []
        self.dfs(pi, True, pi.left, set(to_delete), acc)
        if pi.left:
            acc.append(pi.left)

        return acc

    def dfs(self, pi, is_left, cur, to_delete, acc):
        if cur.left:
            self.dfs(cur, True, cur.left, to_delete, acc)
        if cur.right:
            self.dfs(cur, False, cur.right, to_delete, acc)

        # after dfs delete the child
        if cur.val in to_delete:
            if cur.left:
                acc.append(cur.left)

            if cur.right:
                acc.append(cur.right)

            if is_left:
                pi.left = None
            else:
                pi.right = None
        