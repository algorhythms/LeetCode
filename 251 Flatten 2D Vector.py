"""
Premium Question.
"""
__author__ = 'Daniel'


class Vector2D:
    def __init__(self, vec2d):
        """
        :type vec2d: list[list[int]]
        :type: None
        """
        self.vec2d = vec2d
        self.i = 0
        self.j = 0

    def next(self):
        """

        :rtype: int
        """
        ret = None
        if self.hasNext():
            ret = self.vec2d[self.i][self.j]
            self.j += 1

        return ret

    def hasNext(self):
        """
        This function structures the two pointers.
        :rtype: bool
        """
        # update
        while self.i < len(self.vec2d) and self.j >= len(self.vec2d[self.i]):
            self.i += 1
            self.j = 0

        return self.i < len(self.vec2d) and self.j < len(self.vec2d[self.i])
