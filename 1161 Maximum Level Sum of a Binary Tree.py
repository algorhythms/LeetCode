"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5
"""
import sys 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        bfs
        """
        level = 1
        q = [root]
        maxa = -sys.maxsize-1
        maxlevel = 1
        while q:
            new_q = []
            cur = 0
            for e in q:
                cur += e.val 
                if e.left:
                    new_q.append(e.left)
                if e.right:
                    new_q.append(e.right)
            
            if cur > maxa:
                maxlevel = level
                maxa = cur

            q = new_q
            level += 1
        
        return maxlevel    
