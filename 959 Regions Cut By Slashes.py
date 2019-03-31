#!/usr/bin/python3
"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \,
or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.


Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/,
and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\,
and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:



Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""
from typing import List


class DisjointSet:
    def __init__(self):
        """
        unbalanced DisjointSet
        """
        self.pi = {}

    def union(self, x, y):
        pi_x = self.find(x)
        pi_y = self.find(y)
        self.pi[pi_y] = pi_x

    def find(self, x):
        # LHS self.pi[x]
        if x not in self.pi:
            self.pi[x] = x
        if self.pi[x] != x:
            self.pi[x] = self.find(self.pi[x])
        return self.pi[x]

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        """
        in 1 x 1 cell
        3 possibilities
         ___
        |   |
        |___|
         ___
        |  /|
        |/__|
         ___
        |\  |
        |__\|

        4 regions in the
         ___
        |\ /|
        |/_\|
        """
        m, n = len(grid), len(grid[0])
        ds = DisjointSet()
        T, R, B, L = range(4)  # top, right, bottom, left
        for i in range(m):
            for j in range(n):
                e = grid[i][j]
                if e == "/" or e == " ":
                    ds.union((i, j, B), (i, j, R))
                    ds.union((i, j, T), (i, j, L))
                if e == "\\" or e == " ":  # not elif
                    ds.union((i, j, T), (i, j, R))
                    ds.union((i, j, B), (i, j, L))
                # nbr
                if i - 1 >= 0:
                    ds.union((i, j, T), (i-1, j, B))
                if j - 1 >= 0:
                    ds.union((i, j, L), (i, j-1, R))

                # unnessary, half closed half open
                # if i + 1 < m:
                #     ds.union((i, j, B), (i+1, j, T))
                # if j + 1 < n:
                #     ds.union((i, j, R), (i, j+1, L))


        return len(set(
            ds.find(x)
            for x in ds.pi.keys()
        ))


if __name__ == "__main__":
    assert Solution().regionsBySlashes([
          " /",
          "/ "
        ]) == 2
    assert Solution().regionsBySlashes([
          "//",
          "/ "
        ]) == 3
