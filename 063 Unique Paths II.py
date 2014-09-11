"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
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

        path = [[0 for _ in range(n)] for _ in range(m)]  # possible to optimize by [[0 for _ in range(n+1)]]
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
    assert Solution().uniquePathsWithObstacles(grid)==0

