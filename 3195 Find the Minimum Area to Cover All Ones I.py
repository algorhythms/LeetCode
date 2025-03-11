"""
You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

 

Example 1:

Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:



The smallest rectangle has a height of 2 and a width of 3, so it has an area of 2 * 3 = 6.

Example 2:

Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:



The smallest rectangle has both height and width 1, so its area is 1 * 1 = 1.

 

Constraints:

1 <= grid.length, grid[i].length <= 1000
grid[i][j] is either 0 or 1.
The input is generated such that there is at least one 1 in grid.
"""
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        """
        projection
        O(N^2)
        """
        m = len(grid)
        n = len(grid[0])
        H = [0 for _ in range(n)]
        V = [0 for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    V[i] = 1
                    H[j] = 1
        
        return self.find_l(H) * self.find_l(V)
    
    def find_l(self, A):
        m = len(A)
        lo = -1  # index of last 0
        for i in range(m):
            if A[i] == 1:
                break
            else:
                lo = i

        hi = m  
        for i in range(m-1, -1, -1):
            if A[i] == 1:
                break
            else:
                hi = i

        if lo < hi:
            return (hi-1) - (lo+1) + 1
        
        return 0
