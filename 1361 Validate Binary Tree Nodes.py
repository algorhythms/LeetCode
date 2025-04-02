"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:


Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:


Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false
 

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 10^4
-1 <= leftChild[i], rightChild[i] <= n - 1
"""
from collections import defaultdict


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """
        graph visit to check repeatetion, disconnetion, single root
        """
        has_parent = [False for _ in range(n)]
        visited = [False for _ in range(n)]
        G = defaultdict(list)
        for i in range(n):
            if leftChild[i] >= 0:
                has_parent[leftChild[i]] = True
                G[i].append(leftChild[i])
            if rightChild[i] >= 0:
                has_parent[rightChild[i]] = True
                G[i].append(rightChild[i])                
        
        root = None
        for i in range(n):
            if not has_parent[i]:
                if root is None:
                    root = i
                else:
                    return False
        
        if root is None:
            return False

        self.ret = True
        self.dfs(G, root, visited)
        if not self.ret:
            return False

        for i in range(n):
            if not visited[i]:
                return False

        return True

        
    def dfs(self, G, cur, visited):
        if visited[cur]:
            self.ret = False
            return 
        
        visited[cur] = True
        for nbr in G[cur]:
            self.dfs(G, nbr, visited)