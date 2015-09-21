"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
"""
__author__ = 'Daniel'


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nxt = None
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.nxt:
            self.nxt = self.iterator.next()

        return self.nxt

    def next(self):
        """
        :rtype: int
        """
        ret = self.peek()
        self.nxt = None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nxt is not None or self.iterator.hasNext()
