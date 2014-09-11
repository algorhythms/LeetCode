"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A
gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
"""
__author__ = 'Danyang'
class Solution:
    def grayCode(self, n):
        """
        Graycode: The reflected binary code solves this problem by changing only one switch at a time, so there is never
        any ambiguity of position,
        Dec  Gray   Binary
         0   000    000
         1   001    001
         2   011    010
         3   010    011
         4   110    100
         5   111    101
         6   101    110
         7   100    111


        Algorithm:
        Dec  Gray   Binary
         0     0    000
         1     1    001

         2    11    010
         3    10    011

         4   110    100
         5   111    101
         6   101    110
         7   100    111

        k-bit graycodes is the reversed sequence of (k-1)-bit graycodes appending 1 at the most significant bit
        :param n:
        :return: list of integers (dec_repr)
        """
        if n==0:
            return [0]
        result = [0, 1]

        for num_of_bit in range(2, n+1):
            msb = 1<<num_of_bit-1
            for element in reversed(result):
                result.append(msb+element)

        return result


    def grayCode_math(self, n):
        """
        a-th gray code is a>>1 XOR a
        :param n:
        :return: list of integers (dec_repr)
        """
        return [(x>>1)^x for x in xrange(1<<n)]
