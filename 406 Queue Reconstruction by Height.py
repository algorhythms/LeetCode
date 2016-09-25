"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person who have a height greater
than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
from collections import defaultdict

__author__ = 'Daniel'


class Node(object):
    def __init__(self, lo, hi, cnt):
        self.lo = lo
        self.hi = hi
        self.cnt = cnt  # size of empty slots

        self.left = None
        self.right = None

    def __repr__(self):
        return repr("[%d,%d)" % (self.lo, self.hi))


class SegmentTree(object):
    """empty space"""

    def __init__(self):
        self.root = None

    def build(self, lo, hi):
        """a node can have right ONLY IF has left"""
        if lo >= hi: return
        if lo == hi-1: return Node(lo, hi, 1)

        root = Node(lo, hi, hi-lo)
        root.left = self.build(lo, (hi+lo)/2)
        root.right = self.build((lo+hi)/2, hi)
        return root

    def find_delete(self, root, sz):
        """
        :return: index
        """
        root.cnt -= 1
        if not root.left:
            return root.lo
        elif root.left.cnt >= sz:
            return self.find_delete(root.left, sz)
        else:
            return self.find_delete(root.right,
                                    sz-root.left.cnt)


class Solution(object):
    def reconstructQueue(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        def cmp(a, b):
            if a[0] != b[0]:
                return a[0]-b[0]
            else:
                return a[1]-b[1]

        st = SegmentTree()
        n = len(A)
        st.root = st.build(0, n)
        A.sort(cmp=cmp)
        ret = [0]*n
        ret_cnt = defaultdict(int)  # handle duplicate element
        for a in A:
            val, inv = a
            idx = st.find_delete(st.root, inv+1-ret_cnt[val])
            ret_cnt[val] += 1
            ret[idx] = a

        return ret


if __name__ == "__main__":
    assert Solution().reconstructQueue(
        [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]) == [[3, 0], [6, 0], [7, 0],
                                                                                              [5, 2], [3, 4], [5, 3],
                                                                                              [6, 2], [2, 7], [9, 0],
                                                                                              [1, 9]]