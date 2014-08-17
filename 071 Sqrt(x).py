__author__ = 'Danyang'
class Solution:
    def sqrt(self, x):
        """
        Newton's method
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