"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 10^5
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        """
        find the LCA first, then reconstruct the path

        do it one path 
        dfs -> has_start, has_dest, path
        path use LR, it can degrade to U
        path to itself
        """
        self.start = startValue
        self.dest = destValue
        self.ret = None
        self.dfs(root)
        return self.ret


    def dfs(self, cur):
        if not cur:
            return (False, False, [])

        s = False
        d = False
        p = []
        if cur.val == self.start:
            s = True
        if cur.val == self.dest:
            d = True
        
        ls, ld, lp = self.dfs(cur.left)
        rs, rd, rp = self.dfs(cur.right)
        if (ls ^ rs ^ s) & (ld ^ rd ^ d) & self.ret is None:
            if ls:
                builder = ["U" for _ in lp]
                builder.append("U")
                if rd:
                    builder.append("R")
                    builder += rp[::-1]
                self.ret = "".join(builder)
            elif rs:
                builder = ["U" for _ in rp]
                builder.append("U")
                if ld:
                    builder.append("L")
                    builder += lp[::-1]
                self.ret = "".join(builder)
            elif s:
                builder = []
                if ld:
                    builder.append("L")
                    builder += lp[::-1]
                else:
                    builder.append("R")
                    builder += rp[::-1]
                self.ret = "".join(builder)
                
        if s | d:
            p = []
        elif ls | ld:
            p = lp
            p.append("L")
        elif rs | rd:
            p = rp
            p.append("R")
        
        return (
            ls | rs | s, 
            ld | rd | d, 
            p
        )