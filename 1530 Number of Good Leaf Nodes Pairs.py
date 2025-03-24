"""
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.


Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
 

Constraints:

The number of nodes in the tree is in the range [1, 210].
1 <= Node.val <= 100
1 <= distance <= 10
"""
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        """
        Start DFS from leaf. Create a graph?

        LCA left * right
        maintain a counter: distance -> #leaves
        """
        self.ret = 0
        self.dist = distance
        self.dfs(root)
        return self.ret 
    
    def dfs(self, node):
        """
        return a map of distance to the cur node
        """
        counter = defaultdict(int)
        if not node:
            return counter
        
        if not node.left and not node.right:
            counter[0] = 1
            return counter

        left = self.dfs(node.left)
        right = self.dfs(node.right) 
        for k, v in left.items():
            for K, V in right.items():
                if (k+1) + (K+1) <= self.dist:
                    self.ret += v * V
        
        # merge
        for k, v in left.items():
            k += 1
            if k <= self.dist:
                counter[k] += v
        for k, v in right.items():
            k += 1
            if k <= self.dist:
                counter[k] += v

        return counter

        