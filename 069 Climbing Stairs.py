__author__ = 'Danyang'
class Solution:
    def climbStairs(self, n):
        """
        DP. The transition function should be:
        f(n) = f(n-1) + f(n-2)  n>2;
        or = 1   n=1
        or  = 2   n=2
        :param n: an integer, number of stairs
        :return: an integer, number of different combinations
        """
        f_n_minus_2 = 1  # f(1)
        f_n_minus_1 = 2  # f(2)
        if n==1: return f_n_minus_2
        if n==2: return f_n_minus_1
        fn = 0
        for i in range(2, n):
            fn = f_n_minus_1 +f_n_minus_2
            # for next iteration, n = n+1
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = fn
        return fn

if __name__=="__main__":
    print Solution().climbStairs(3)