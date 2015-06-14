"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon
consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and
must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or
below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other
rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each
step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path
RIGHT-> RIGHT -> DOWN -> DOWN.

-2(K) -3	3
-5    -10	1
10	  30   -5(P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the
princess is imprisoned.
"""
__author__ = 'Daniel'
import sys


class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        dp
        Let F represent the HP
        Starting backward
        DP transition function:
        path = min(F[i+1][j], F[i][j+1])  # choose the right or down path with minimum HP required
        F[i][j] = max(1, path-dungeon[i][j])  # adjust for current cell

        :type dungeon: list[list[int]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])

        F = [[sys.maxint for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    F[i][j] = max(1, 1-dungeon[i][j])
                else:
                    path = min(F[i+1][j], F[i][j+1])  # choose the path with minimum HP required
                    F[i][j] = max(1, path-dungeon[i][j])  # adjust for current cell

        return F[0][0]

    def calculateMinimumHP_error(self, dungeon):
        """
        dp
        Not just the end results. We have to ensure at every cell the life > 0.
        Starting forward
        :type dungeon: list[list[int]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:
            return 1-min(0, dungeon[0][0])

        F = [[-sys.maxint-1 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if i == 1 and j == 1:
                    F[i][j] = dungeon[i-1][j-1]
                else:
                    F[i][j] = max(F[i-1][j], F[i][j-1])+dungeon[i-1][j-1]
                    F[i][j] = min(F[i][j], dungeon[i-1][j-1])

        return 1-F[-1][-1]


if __name__ == "__main__":
    assert Solution().calculateMinimumHP([[-3, 5]]) == 4
    assert Solution().calculateMinimumHP([[2, 1], [1, -1]]) == 1
