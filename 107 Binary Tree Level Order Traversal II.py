"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by
level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        bfs
        :param root: TreeNode
        :return: Integers
        """
        if not root:
            return []
        result = []
        next_level = [root]
        while next_level:
            current_level = next_level
            result.insert(0, map(lambda x: x.val, current_level))  # current level, only difference with Binary Tree Level Order Traversal I

            next_level = []
            for element in current_level:
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
        return result

if __name__=="__main__":
    Solution().levelOrderBottom(TreeNode(1))










