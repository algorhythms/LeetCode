"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
"""
__author__ = 'Danyang'
class Solution:
    def uniquePaths(self, m, n):
        """
        dp
        path[i][j] = path[i-1][j] + path[i][j-1]
        :param m:
        :param n:
        :return: an integer
        """
        path = [[0 for _ in range(n)] for _ in range(m)]
        path[0][0]  = 1 # start

        # path[i][j] = path[i-1][j] + path[i][j-1]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i==0:
                    path[i][j] = path[i][j-1]
                elif j==0:
                    path[i][j] = path[i-1][j]
                else:
                    path[i][j] = path[i-1][j]+path[i][j-1]
        return path[m-1][n-1]

if __name__=="__main__":
    print Solution().uniquePaths(3, 7)