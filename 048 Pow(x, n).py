"""
Implement pow(x, n).
"""
__author__ = 'Danyang'


class Solution:
    def pow(self, x, n):
        """
        O(log n)
        Algorithm: math, Exponentiation by Squaring

        Basically: x^n = (x^2)^(n/2)
        More formally: x^n = x^(n/2) * x^(n/2) * x^(n%2)

        :param x: float
        :param n: integer
        :return: float
        """
        invert_flag = False if n > 0 else True
        # O(log n)
        n = abs(n)
        product = 1.0
        while n > 0:
            if n & 1 == 1:
                product *= x

            n = n >> 1
            x *= x

        if invert_flag:
            product = 1.0 / product

        return product

    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow_TLE(self, x, n):
        """
        O(n)
        """
        if abs(x)<=0.00001:
            return 0
        if x==1.0:
            return 1
        if x==-1.0:
            if n&1==1:
                return 1
            else:
                return -1

        if abs(x-1.0)<1e-6:
            return 1+(x-1.0)*n

        if abs(x--1.0)<1e-6:
            if n % 2==0:
                return self.pow(-x, n)
            else:
                return -self.pow(-x, n)

        product = 1.0
        for i in xrange(abs(n)):
            pre = product
            if n>0:
                product *= x
            else:
                product /= x

            if abs(product - pre)<1e-5:
                break

        return product


if __name__=="__main__":
    print Solution().pow(8.88023, 3)
