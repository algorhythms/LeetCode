"""
Premium Question
"""
__author__ = 'Daniel'


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.mat = [v1, v2]
        self.maxa = max((c, r) for r, c in enumerate(map(lambda x: len(x)-1, self.mat)))
        self.i = 0
        self.j = 0
        self._reposition()

    def _reposition(self):
        while self.i >= len(self.mat) or self.j >= len(self.mat[self.i]):
            if not self.hasNext():
                return

            elif self.i >= len(self.mat):
                self.i = 0
                self.j += 1

            elif self.j >= len(self.mat[self.i]):
                self.i += 1

    def next(self):
        """
        :rtype: int
        """
        if not self.hasNext():
            raise StopIteration

        ret = self.mat[self.i][self.j]
        self.i += 1
        self._reposition()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.j <= self.maxa[0]


if __name__ == "__main__":
    v1 = [1, 2]
    v2 = [3, 4, 5, 6]
    itr = ZigzagIterator(v1, v2)
    while itr.hasNext():
        print itr.next()