"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""
import math

__author__ = 'Daniel'


class Solution:
    def countPrimes(self, n):
        """
        Find prime using Sieve's algorithm
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        is_prime = [True for _ in xrange(n)]
        is_prime[0], is_prime[1] = False, False
        for i in xrange(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for j in xrange(i*i, n, i):
                    is_prime[j] = False

        return is_prime.count(True)


if __name__ == "__main__":
    assert Solution().countPrimes(1500000) == 114155