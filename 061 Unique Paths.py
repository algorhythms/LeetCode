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