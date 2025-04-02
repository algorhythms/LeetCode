"""
Two players play a turn based game on a binary tree. We are given the root of this binary tree, and the number of nodes n in the tree. n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x. The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player. In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn. If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player. If it is possible to choose such a y to ensure you win the game, return true. If it is not possible, return false.

 

Example 1:


Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
Example 2:

Input: root = [1,2,3], n = 3, x = 1
Output: false
 

Constraints:

The number of nodes in the tree is n.
1 <= x <= n <= 100
n is odd.
1 <= Node.val <= n
All the values of the tree are unique.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTwoPasses:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        """
        taking control of the root with larger subtree 
        block the parent, left or right 
        """
        self.root_count = self.count(root)
        self.ret = False
        self.dfs(root, x)
        return self.ret 

    def count(self, cur):
        if not cur:
            return 0
        
        s = 1
        s += self.count(cur.left)
        s += self.count(cur.right)
        return s
    
    def dfs(self, cur, x):
        if not cur:
            return 0

        l = self.dfs(cur.left, x)        
        r = self.dfs(cur.right, x)
        c = l + r + 1
        if cur.val == x:
            # block left:
            if l > self.root_count - l:
                self.ret = True
            # block right
            if r > self.root_count - r:
                self.ret = True
            # block parent:
            if self.root_count - c > c:
                self.ret = True

        return c
    

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        self.x_left = 0
        self.x_right = 0
        self.x_root = 0
        root_count = self.dfs(root, x)
        
        if self.x_left > root_count - self.x_left:
            return True
        if self.x_right > root_count - self.x_right:
            return True
        if root_count - self.x_root > self.x_root:
            return True
        return False


    def dfs(self, cur, x):
        if not cur:
            return 0
        
        l = self.dfs(cur.left, x)
        r = self.dfs(cur.right, x)
        c = 1 + l + r
        if cur.val == x:
            self.x_left = l
            self.x_right = r
            self.x_root = c
        
        return c