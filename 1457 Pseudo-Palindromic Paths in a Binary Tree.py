"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.

 

Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1 
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 9
"""
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTLE:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        DFS 
        travel to leave 
        maintain a counter to check for palindrom
        """
        self.ret = 0
        self.dfs(root, [])
        return self.ret
    
    def dfs(self, node, stk):
        if not node:
            return 
        
        stk.append(node.val)
        if not node.left and not node.right:
            if self.is_palindrom(stk):
                self.ret += 1
        
        self.dfs(node.left, stk)
        self.dfs(node.right, stk)
        stk.pop()
        
    def is_palindrom(self, stk):
        counter = defaultdict(int)
        for e in stk:
            counter[e] += 1
        
        has_odd = False
        for cnt in counter.values():
            if cnt % 2 == 1:
                if has_odd:
                    return False
                else:
                    has_odd = True
        
        return True
        

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        DFS 
        travel to leave 
        maintain a counter to check for palindrom
        """
        self.ret = 0
        self.dfs(root, defaultdict(int))
        return self.ret
    
    def dfs(self, node, counter):
        if not node:
            return 
        
        counter[node.val] += 1
        if not node.left and not node.right:
            if self.is_palindrom(counter):
                self.ret += 1
        
        self.dfs(node.left, counter)
        self.dfs(node.right, counter)
        counter[node.val] -= 1
        
    def is_palindrom(self, counter):
        has_odd = False
        for cnt in counter.values():
            if cnt % 2 == 1:
                if has_odd:
                    return False
                else:
                    has_odd = True
        
        return True