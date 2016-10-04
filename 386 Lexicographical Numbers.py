"""
Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""
__author__ = 'Daniel'


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def gen():
            i = 1
            for _ in xrange(n):  # erroneous for while i <= n:
                yield i
                if i * 10 <= n:
                    i *= 10  # * 10
                elif i % 10 != 9 and i + 1 <= n:
                    i += 1  # for current digit
                else:
                    while i % 10 == 9 or i + 1 > n:
                        i /= 10
                    i += 1

        return list(gen())

    def lexicalOrderError(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        for i in xrange(1, 10):
            sig = 1
            while i * sig <= n:
                ret.extend(range(
                    i * sig,
                    min((1+i)*sig-1, n)+1),
                )
                sig *= 10

        return ret


if __name__ == "__main__":
    assert Solution().lexicalOrder(30) == [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27,
                                           28, 29, 3, 30, 4, 5, 6, 7, 8, 9]
