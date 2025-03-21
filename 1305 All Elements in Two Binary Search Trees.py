"""
Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-10^5 <= Node.val <= 10^5
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        """
        maintain two lists and 
        like merge sort, morris traversal? 
        """
        gen1 = self.morris(root1)
        gen2 = self.morris(root2)
        ret = []
        a = next(gen1, None) 
        b = next(gen2, None)
        # None is different from 0
        while a is not None or b is not None:
            if a is not None and b is not None:
                if a > b:
                    ret.append(b)
                    b = next(gen2, None)
                else:
                    ret.append(a)
                    a = next(gen1, None)
            elif a is not None:
                ret.append(a)
                a = next(gen1, None)
            else:
                ret.append(b)
                b = next(gen2, None)
        
        return ret        
    
    def morris(self, cur):
        while cur:
            if not cur.left:
                yield cur.val
                cur = cur.right 
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    yield cur.val
                    cur = cur.right
