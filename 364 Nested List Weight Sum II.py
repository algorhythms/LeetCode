"""
Premium Question
"""
__author__ = 'Daniel'


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
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

    def depthSumInverse(self, nestedList):
        """
        NestedInteger is a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        inv_depth = self.height(nestedList)
        self.inverseDepthSum(nestedList, inv_depth)
        return self.sum

    def height(self, nl):
        nl_lst = filter(lambda x: not x.isInteger(), nl)
        if not nl_lst:
            return 1
        if nl_lst:
            return 1 + max(
                map(lambda x: self.height(x.getList()), nl_lst)
            )

    def inverseDepthSum(self, nl, inv_depth):
        nl_lst = filter(lambda x: not x.isInteger(), nl)
        ni_list = filter(lambda x: x.isInteger(), nl)
        if nl_lst:
            map(lambda x: self.inverseDepthSum(x.getList(), inv_depth - 1), nl_lst)
        if ni_list:
            self.sum += sum(map(lambda x: x.getInteger() * inv_depth, ni_list))


class SolutionError(object):
    def __init__(self):
        self.sum = 0

    def depthSumInverse(self, nestedList):
        """
        NestedInteger is a union type
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        self.dfs(nestedList)
        return self.sum

    def dfs(self, nl):
        """
        This dfs use height: the number of edges from to the leaves.
        But the question is supposedly use height but the calculate sum top down; here is bottom up wrongly.
        """
        height = 1

        nl_lst = filter(lambda x: not x.isInteger(), nl)
        ni_list = filter(lambda x: x.isInteger(), nl)
        if nl_lst:
            height = 1 + max(
                map(lambda x: self.dfs(x.getList()), nl_lst)
            )
        if ni_list:
            self.sum += sum(map(lambda x: x.getInteger() * height, ni_list))

        return height
