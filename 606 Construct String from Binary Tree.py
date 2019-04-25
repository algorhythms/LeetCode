#!/usr/bin/python3
"""
You need to construct a string consists of parenthesis and integers from a
binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you
need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping
relationship between the input and the output.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        ret = [str(t.val)]
        if left or right:
            ret.append("(" + left + ")")
        if right:
            ret.append("(" + right + ")")

        return "".join(ret)
