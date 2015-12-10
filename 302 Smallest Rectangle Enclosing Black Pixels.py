"""
Premium Question
Projection and bisect
"""
import bisect
__author__ = 'Daniel'


class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        yaxis = [
            1 if any(image[i][j] == "1" for i in xrange(m)) else 0
            for j in xrange(n)
        ]
        xaxis = [
            1 if any(image[i][j] == "1" for j in xrange(n)) else 0
            for i in xrange(m)
        ]

        y_lo = bisect.bisect_left(yaxis, 1, 0, y)
        y_hi = bisect.bisect_left(map(lambda e: 1^e, yaxis), 1, y)  # bisect must be sorted
        x_lo = bisect.bisect_left(xaxis, 1, 0, x)
        x_hi = bisect.bisect_left(map(lambda e: 1^e, xaxis), 1, x)
        return (y_hi-y_lo)*(x_hi-x_lo)


if __name__ == "__main__":
    image = [
        "00",
        "10",
    ]

    assert Solution().minArea(image, 1, 0) == 1