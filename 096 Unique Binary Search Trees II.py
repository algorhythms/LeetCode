"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
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

    def generateTrees(self, n):
        """
        dfs
        Catalan
        :param n: integer
        :return: list of TreeNode
        """
        if n==0:
            return [None]

        return self.generate(1, n)

    def generate(self, start, end):
        """
        dfs without dp
        :param start: initial number in the array
        :param end: final number in the array
        :return: list of TreeNode
        """
        sub_trees = []

        # trivial
        if start>end:
            sub_trees.append(None)
            return sub_trees

        # pivot
        # list of unique subtrees = list of unique left subtrees, pivot, list of unique right subtrees
        for pivot in range(start, end+1):
            left_sub_trees = self.generate(start, pivot-1)  # no dp yet
            right_sub_trees = self.generate(pivot+1, end)  # no dp yet
            for left_node in left_sub_trees:
                for right_node in right_sub_trees:
                    pivot_node = TreeNode(pivot)
                    pivot_node.left = left_node
                    pivot_node.right = right_node
                    sub_trees.append(pivot_node)


        return sub_trees


