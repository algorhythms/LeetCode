"""
Premium Question
"""
__author__ = 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution(object):
    def __init__(self):
        self.sum = 0

    def depthSum(self, nestedList):
        """
        NestedInteger is  a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        for elt in nestedList:
            self.dfs(elt, 1)

        return self.sum

    def dfs(self, ni, depth):
        if ni.isInteger():
            self.sum += ni.getInteger() * depth
        else:
            lst = ni.getList()
            for elt in lst:
                self.dfs(elt, depth + 1)
