"""
Implement int sqrt(int x).

Compute and return the square root of x.
"""
__author__ = 'Danyang'
class Solution:
    def sqrt(self, x):
        """
        Newton's method
        x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \

        http://en.wikipedia.org/wiki/Newton's_method
        :param x: Integer
        :return: Integer
        """
        if x==0: return 0  # avoid Division by zero
        m = x
        while True:
            m_before = m
            m = m - float(m*m-x)/(2*m)
            if abs(m-m_before)<1e-7: break

        return int(m)

if __name__=="__main__":
    print Solution().sqrt(2)