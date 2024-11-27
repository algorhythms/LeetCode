#!/usr/bin/python3
"""
You are given a tree rooted at node 0 that consists of n nodes numbered from 0 to n - 1. The tree is represented by an array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

We make the following changes on the tree one time simultaneously for all nodes x from 1 to n - 1:

Find the closest node y to node x such that y is an ancestor of x, and s[x] == s[y].
If node y does not exist, do nothing.
Otherwise, remove the edge between x and its current parent and make node y the new parent of x by adding an edge between them.
Return an array answer of size n where answer[i] is the size of the 
subtree
 rooted at node i in the final tree.

 

Example 1:

Input: parent = [-1,0,0,1,1,1], s = "abaabc"

Output: [6,3,1,1,1,1]

Explanation:


The parent of node 3 will change from node 1 to node 0.

Example 2:

Input: parent = [-1,0,4,0,1], s = "abbba"

Output: [5,2,1,1,1]

Explanation:


The following changes will happen at the same time:

The parent of node 4 will change from node 1 to node 0.
The parent of node 2 will change from node 4 to node 1.
 

Constraints:

n == parent.length == s.length
1 <= n <= 10^5
0 <= parent[i] <= n - 1 for all i >= 1.
parent[0] == -1
parent represents a valid tree.
s consists only of lowercase English letters.
"""
from collections import defaultdict


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        """
        Naively dfs updating the tree results in TLE of O(N^2).
        Need to do a topological dfs update on the tree for O(N).
        * Does not require `visited` in topological sort since it's acyclic tree
        * The `path` holds the map of a list of ancestors with a given char, with the last one as the closest
        """
        G = defaultdict(list)
        for i, pi in enumerate(parent):
            G[pi].append(i)

        self.topo(G, 0, defaultdict(list), parent, s)

        G = defaultdict(list)
        for i, pi in enumerate(parent):
            G[pi].append(i)
        
        ret = [0 for _ in range(len(parent))]
        self.dfs(G, 0, ret)
        return ret
        
    def topo(self, G, cur, path, parent, s):
        # topological dfs
        char = s[cur]
        if len(path[char]) > 0:
            pi = path[char][~0]  # or path[char][-1]
            parent[cur] = pi
        
        path[char].append(cur)
        for v in G[cur]:
            self.topo(G, v, path, parent, s)
        path[char].pop()

    def dfs(self, G, cur, ret):
        # compute size
        sz = 1
        for v in G[cur]:
            sz += self.dfs(G, v, ret)

        ret[cur] = sz
        return sz



class SolutionTLE:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        """
        Just do the operation
        index 0 is always the root

        To get sub tree size, we can 
        1. convert to TreeNode
        2. Sort pi array and then count. It does not work. It is not necessary pi > i
        """
        new_parent = list(parent)  # clone 
        for i in range(len(parent)):
            pi = parent[i]  # index
            while pi != -1 and s[pi] != s[i]:
                pi = parent[pi]
                
            if pi != -1:
                new_parent[i] = pi
        
        return self.find_size(new_parent)
    
    def find_size(self, parent):
        G = defaultdict(list)
        for i, pi in enumerate(parent):
            G[pi].append(i)

        ret = [0 for _ in parent]
        self.dfs(G, 0, ret)
        return ret

    def dfs(self, G, i, ret):
        sz = 1
        for v in G[i]:
            sz += self.dfs(G, v, ret)

        ret[i] = sz
        return sz

    def find_size_wrong(self, parent):
        # compute size
        sz = [1 for _ in parent]
        parent = [(pi, i) for i, pi in enumerate(parent)]
        for pi, i in sorted(parent, reverse=True):
            if pi != -1:
                sz[pi] += sz[i]

        return sz
