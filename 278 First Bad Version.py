"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.
"""
__author__ = 'Daniel'


def isBadVersion(version):
    pass


class Solution(object):
    def firstBadVersion(self, n):
        """
        :param n: An integers.
        :return: An integer which is the first bad version.
        """
        l = 1
        h = n+1
        while l < h:
            m = (l+h)/2
            if not isBadVersion(m):
                l = m+1
            else:
                h = m

        return l