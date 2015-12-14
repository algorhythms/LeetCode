"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where
counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
"""
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, start, end, cnt=0):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left = None
        self.right = None


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n)

    def build(self, start, end):
        if start >= end: return
        if start == end-1: return TreeNode(start, end)
        node = TreeNode(start, end)
        node.left = self.build(start, (start+end)/2)
        node.right = self.build((start+end)/2, end)
        return node

    def inc(self, idx, val):
        cur = self.root
        while cur:
            cur.cnt += val
            mid = (cur.start+cur.end)/2
            if cur.start <= idx < mid:
                cur = cur.left
            elif mid <= idx < cur.end:
                cur = cur.right
            else:
                return

    def query_less(self, cur, idx):
        if not cur:
            return 0

        mid = (cur.start+cur.end)/2
        if cur.start <= idx < mid:
            return self.query_less(cur.left, idx)
        elif mid <= idx < cur.end:
            return (cur.left.cnt if cur.left else 0) + self.query_less(cur.right, idx)
        else:
            return 0


class Solution(object):
    def countSmaller(self, nums):
        """
        Brute force: O(n^2)
        Segment Tree
        O(n lg n)
        :type nums: List[int]
        :rtype: List[int]
        """
        # preprocess the array to make it discrete in [0, 1, ..., n-1]
        h = {}
        for i, v in enumerate(sorted(nums)):
            h[v] = i  # override duplicates

        A = [h[v] for v in nums]
        n = len(A)
        st = SegmentTree(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            ret.append(st.query_less(st.root, A[i]))
            st.inc(A[i], 1)

        return ret[::-1]


if __name__ == "__main__":
    assert Solution().countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert Solution().countSmaller([-1, -1]) == [0, 0]
