#!/usr/bin/python3
"""
We want to use quad trees to store an N x N boolean grid. Each cell in the grid
can only be true or false. The root node represents the whole grid. For each
node, it will be subdivided into four children nodes until the values in the
region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if
and only if the node is a leaf node. The val attribute for a leaf node contains
the value of the region it represents.
"""
__author__ = 'Danyang'


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        """
        DPS, check 4 children then merge

        :type grid: List[List[int]]
        :rtype: Node
        """
        l = len(grid)
        return self._construct(grid, 0, 0, l)

    def _construct(self, grid, row, col, l):
        """
        Use row col for matrix rather than x y coordiate since the direction is
        error-prone
        """
        if l == 1:
            return Node(grid[row][col], True, None, None, None, None)

        l_child = l // 2
        topLeft = self._construct(grid, row, col, l_child)
        topRight = self._construct(grid, row, col + l_child, l_child)
        bottomLeft = self._construct(grid, row + l_child, col, l_child)
        bottomRight = self._construct(grid, row + l_child, col + l_child, l_child)
        is_leaf = (
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            != "*"
        )
        if is_leaf:
            return Node(grid[row][col], True, None, None, None, None)

        return Node("*", False, topLeft, topRight, bottomLeft, bottomRight)
