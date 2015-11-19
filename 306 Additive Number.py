"""
Additive number is a positive integer whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent
number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string represents an integer, write a function to determine if it's an additive number.
"""
__author__ = 'Daniel'


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        Backtracking
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in xrange(1, n):
            for j in xrange(i, n):
                if self.predicate(num, 0, i, j):
                    return True

        return False

    def predicate(self, s, b, i, j):
        n1 = s[b:i]
        n2 = s[i:j]

        if b != 0 and j == len(s):
            return True
        if not n1 or not n2:
            return False
        if len(n1) > 1 and n1[0] == '0' or len(n2) > 1 and n2[0] == '0':
            return False

        n3 = str(int(n1)+int(n2))
        J = j+len(n3)
        if s[j:J] == n3:
            return self.predicate(s, i, j, J)


if __name__ == "__main__":
    assert Solution().isAdditiveNumber("12012122436")