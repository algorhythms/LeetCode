"""
Premium Question
"""
__author__ = 'Daniel'


def read4(buf):
    """
    read 4 chars to buf

    :type buf: List[str]
    :rtype: int
    """
    return 0


class Solution(object):
    def read(self, buf, n):
        """
        read n chars to buf
        Algorithm:
        Two dimensions
          1st dim: buf full or not
          2nd dim: buf4 full or not

        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            buf4 = ["" for _ in xrange(4)]
            r = read4(buf4)
            if idx+r < n:
                buf[idx:idx+r] = buf4[:r]
                idx += r
                if r < 4: break
            else:
                buf[idx:n] = buf4[:n-idx]
                idx = n

        return idx
