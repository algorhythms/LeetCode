#!/usr/bin/python3
"""
A complete binary tree is a binary tree in which every level, except possibly
the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary
tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with
head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value
node.val = v so that the tree remains complete, and returns the value of the
parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs =
[[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:
The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class CBTInserter:
    def __init__(self, root: TreeNode):
        """
        Maintain a dequeue of insertion candidates
        Insertion candidates are non-full nodes (superset of leaf nodes)
        BFS to get the insertion candidates

        During insertion, insert the node to the first insertion candidate's
        child. Then, the inserting node is the last in the candidate queue
        """
        self.candidates = deque()
        self.root = root
        q = [root]  # can also use deque
        while q:
            cur_q = []
            for e in q:
                if e.left:
                    cur_q.append(e.left)
                if e.right:
                    cur_q.append(e.right)
                if not e.left or not e.right:
                    # non-full node
                    self.candidates.append(e)
            q = cur_q

    def insert(self, v: int) -> int:
        pi = self.candidates[0]
        node = TreeNode(v)
        if not pi.left:
            pi.left = node
        else:
            pi.right = node

        if pi.left and pi.right:
            self.candidates.popleft()

        self.candidates.append(node)
        return pi.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
