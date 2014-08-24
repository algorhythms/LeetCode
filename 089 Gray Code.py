__author__ = 'Danyang'
class Solution:
    def grayCode(self, n):
        """
        Graycode: The reflected binary code solves this problem by changing only one switch at a time, so there is never any ambiguity of position,
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
        return [(x>>1)^x for x in xrange(1<<n)]
