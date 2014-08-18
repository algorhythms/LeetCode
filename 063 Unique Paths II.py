__author__ = 'Danyang'
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        dp
        :param obstacleGrid:  a list of lists of integers
        :return: integer
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # trivial
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0

        path = [[0 for _ in range(n)] for _ in range(m)]
        path[0][0] = 1 # start

        # path[i][j] = path[i-1][j] + path[i][j-1]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i==0:
                    path[i][j] = path[i][j-1] if obstacleGrid[i][j-1]==0 else 0
                elif j==0:
                    path[i][j] = path[i-1][j] if obstacleGrid[i-1][j]==0 else 0
                else:
                    if obstacleGrid[i][j-1]==0 and obstacleGrid[i-1][j]==0:
                        path[i][j] = path[i-1][j]+path[i][j-1]
                    elif obstacleGrid[i][j-1]==0:
                        path[i][j] = path[i][j-1]
                    elif obstacleGrid[i-1][j]==0:
                        path[i][j] = path[i-1][j]
                    else:
                        path[i][j]=0


        return path[m-1][n-1]

if __name__=="__main__":
    grid = [[0, 0], [1, 1], [0, 0]]
    print Solution().uniquePathsWithObstacles(grid)

