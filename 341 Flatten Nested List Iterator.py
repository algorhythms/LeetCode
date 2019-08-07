"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
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
        return True

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        return 0

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        return []


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        Linear structure usually use stack as structure.
        Iterator Invariant:
        1. has the value to be returned ready: idx pointing to the integer to be return in the next().
        2. rember move the parent pointer in hasNext()

        Possible to compile nl and idx into a tuple.
        """
        self.stk = [[nestedList, 0]]  # stack of iterators

    def next(self):
        """
        :rtype: int
        """
        nl, idx = self.stk[-1]
        nxt = nl[idx].getInteger()
        self.stk[-1][1] = idx + 1  # advance the index
        return nxt

    def hasNext(self):
        """
        Put the pointer movement logic in the hasNext()
        :rtype: bool
        """
        while self.stk:
            nl, idx = self.stk[-1]
            if idx < len(nl):
                ni = nl[idx]
                if ni.isInteger():
                    return True
                else:
                    self.stk[-1][1] = idx + 1  # prepare the parent, otherwise dead loop
                    nxt_nl = ni.getList()
                    self.stk.append([nxt_nl, 0])
            else:
                self.stk.pop()

        return False



class NestedIteratorVerbose(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]

        Iterator Invariant:
        1. has the value to be returned ready: idx pointing to the integer to be return in the next().
        2. move the pointer in hasNext()

        Possible to compile nl and idx into a tuple.
        """
        self.nl_stk = [nestedList]
        self.idx_stk = [0]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            nl = self.nl_stk[-1]
            idx = self.idx_stk[-1]
            nxt = nl[idx]
            self.idx_stk[-1] = idx + 1
            return nxt

        raise StopIteration()

    def hasNext(self):
        """
        Put the pointer movement logic in the hasNext()
        :rtype: bool
        """
        while self.nl_stk:
            nl = self.nl_stk[-1]
            idx = self.idx_stk[-1]
            if idx < len(nl):
                ni = nl[idx]
                if ni.isInteger():
                    return True
                else:
                    self.idx_stk[-1] = idx+1
                    nxt_nl = ni.getList()
                    nxt_idx = 0
                    self.nl_stk.append(nxt_nl)
                    self.idx_stk.append(nxt_idx)
            else:
                self.nl_stk.pop()
                self.idx_stk.pop()

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
