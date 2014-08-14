__author__ = 'Danyang'
class Solution:
    def numTrees(self, n):
        """
        number of unique binary search tree
        Catalan Number
        Proof: http://en.wikipedia.org/wiki/Catalan_number#Second_proof
        :param n: integer
        :return: integer
        """
        return self.factorial(2*n)/(self.factorial(n)*self.factorial(n)) -self.factorial(2*n)/(
            self.factorial(n+1)*self.factorial(n-1))

    def factorial(self, n):
        factorial = 1
        for i in range(n):
            factorial *= i+1
        return factorial
