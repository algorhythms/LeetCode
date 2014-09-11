"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
"""
__author__ = 'Danyang'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        BFS, stack & queue
        :param root: a tree node
        :return:  a list of lists of integers
        """
        if not root:
            return []

        result = []
        lst = [root]
        direction = False
        while lst:
            if direction:
                result.append([element.val for element in lst])
            else:
                result.append([element.val for element in reversed(lst)])

            for i in range(len(lst)):  # evaluation time
                element = lst.pop(0)  # queue 
                if element.left:
                    lst.append(element.left)
                if element.right:
                    lst.append(element.right)
            direction = not direction
        return result


