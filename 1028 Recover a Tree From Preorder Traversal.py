#!/usr/bin/python3
"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this
node), then we output the value of this node.  (If the depth of a node is D, the
depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.


Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]


Example 3:
Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]


Note:
The number of nodes in the original tree is between 1 and 1000.
Each node will have a value between 1 and 10^9.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import OrderedDict


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        """
        map: node -> depth
        stack of pi (incompleted)
        """
        depth = 0
        # parse
        n = len(S)
        i = 0
        root = None
        stk = []
        while i < n:
            if S[i] == "-":
                depth += 1
                i += 1
            else:
                j = i
                while j < n and S[j] != "-":
                    j += 1

                val = int(S[i:j])

                # construct
                cur = TreeNode(val)
                if depth == 0:
                    root = cur
                    stk = [(depth, root)]
                else:
                    assert stk
                    while stk[-1][0] != depth - 1:
                        stk.pop()

                    _, pi = stk[-1]
                    if not pi.left:
                        pi.left = cur
                    elif not pi.right:
                        pi.right = cur
                        stk.pop()
                    else:
                        raise
                    stk.append((depth, cur))

                depth = 0
                i = j

        return root

    def recoverFromPreorder_error(self, S: str) -> TreeNode:
        """
        map: node -> depth
        stack of pi (incompleted)
        """
        depth = 0
        depths = OrderedDict()
        # parse
        n = len(S)
        i = 0
        while i < n:
            if S[i] == "-":
                depth += 1
                i += 1
            else:
                j = i
                while j < n and S[j] != "-":
                    j += 1

                val = int(S[i:j])
                depths[val] = depth
                depth = 0
                i = j

        # construct
        stk = []
        root = None
        for k, v in depths.items():
            cur = TreeNode(k)
            if v == 0:
                root = cur
                stk = [root]
            else:
                assert stk
                while depths[stk[-1].val] != v - 1:
                    stk.pop()

                if not stk[-1].left:
                    stk[-1].left = cur
                elif not stk[-1].right:
                    stk[-1].right = cur
                    stk.pop()
                else:
                    raise
                stk.append(cur)

        return root


if __name__ == "__main__":
    assert Solution().recoverFromPreorder("5-4--4")
    assert Solution().recoverFromPreorder("1-2--3--4-5--6--7")
