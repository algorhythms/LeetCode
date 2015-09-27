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
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while idx < n:
            buf4 = ["" for _ in xrange(4)]
            r = read4(buf4)
            if idx+r < n:
                for i in xrange(r):
                    buf[idx+i] = buf4[i]
                idx += r
                if r < 4:
                    break
            else:
                for i in xrange(n-idx):
                    buf[idx+i] = buf4[i]
                idx = n

        return idx