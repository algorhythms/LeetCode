"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the
second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""
__author__ = 'Daniel'


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype int
        """
        version1 = map(int, version1.split("."))
        version2 = map(int, version2.split("."))
        n1 = len(version1)
        n2 = len(version2)

        for i in xrange(min(n1, n2)):
            if version1[i] == version2[i]:
                pass
            else:
                return -1 if version1[i] < version2[i] else 1

        # 1.0.0 and 1 
        if n1 == n2 or n1 > n2 and all(map(lambda x: x == 0, version1[n2:])) or \
                                n1 < n2 and all(map(lambda x: x == 0, version2[n1:])):
            return 0

        return -1 if n1 < n2 else 1

