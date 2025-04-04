"""
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        DFS
        """
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
        self.dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.maxa = 0
        visited = [
            [False for _ in range(self.N)]
            for _ in range(self.M)
        ]
        for i in range(self.M):
            for j in range(self.N):
                if grid[i][j] != 0:
                    self.dfs(i, j, 0, visited)
        
        return self.maxa
        
    def dfs(self, i, j, path_sum, visited):
        path_sum += self.grid[i][j]
        self.maxa = max(self.maxa, path_sum)
        visited[i][j] = True
        for di, dj in self.dirs:
            I = i + di
            J = j + dj
            if 0 <= I < self.M and 0 <= J < self.N and self.grid[I][J] != 0 and not visited[I][J]:
                self.dfs(I, J, path_sum, visited)

        visited[i][j] = False
        path_sum -= self.grid[i][j]


class SolutionStyle:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        DFS
        """
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
        self.dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.maxa = 0
        visited = [
            [False for _ in range(self.N)]
            for _ in range(self.M)
        ]
        for i in range(self.M):
            for j in range(self.N):
                self.dfs(i, j, 0, visited)
        
        return self.maxa
        
    def dfs(self, i, j, path_sum, visited):
        if self.grid[i][j] == 0 or visited[i][j]:
            return 

        path_sum += self.grid[i][j]
        self.maxa = max(self.maxa, path_sum)
        visited[i][j] = True
        for di, dj in self.dirs:
            I = i + di
            J = j + dj
            if 0 <= I < self.M and 0 <= J < self.N:
                self.dfs(I, J, path_sum, visited)

        visited[i][j] = False
        path_sum -= self.grid[i][j]