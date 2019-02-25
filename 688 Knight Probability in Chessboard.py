#!/usr/bin/python3
"""
On an NxN chessboard, a knight starts at the r-th row and c-th column and
attempts to make exactly K moves. The rows and columns are 0 indexed, so the
top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move
is two squares in a cardinal direction, then one square in an orthogonal
direction.

[Image]

Each time the knight is to move, it chooses one of eight possible moves
uniformly at random (even if the piece would go off the chessboard) and moves
there.

The knight continues moving until it has made exactly K moves or has moved off
the chessboard. Return the probability that the knight remains on the board
after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on
the board.
From each of those positions, there are also two moves that will keep the knight
on the board.
The total probability the knight stays on the board is 0.0625.
"""
dirs = (
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
)


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """
        brute force K step

        with memory, it is considered dp
        """
        q = set([(r, c)])  # working que
        P = [[0 for _ in range(N)] for _ in range(N)]
        P[r][c] = 1  # optimize memory
        k = 0
        while k < K:
            k += 1
            cur_q = set()
            cur_P = [[0 for _ in range(N)] for _ in range(N)]
            for i, j in q:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < N and 0 <= J < N:
                        cur_q.add((I, J))
                        cur_P[I][J] += P[i][j] * 1 / 8

            q = cur_q
            P = cur_P

        return sum([
            P[i][j]
            for i in range(N)
            for j in range(N)
        ])


    def knightProbability_error(self, N: int, K: int, r: int, c: int) -> float:
        """
        brute force K step
        """
        q = [(r, c)]  # working que
        P = [[0 for _ in range(N)] for _ in range(N)]
        P[r][c] = 1  # optimize memory
        k = 0
        while k < K:
            k += 1
            cur_q = []
            cur_P = [[0 for _ in range(N)] for _ in range(N)]
            for i, j in q:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < N and 0 <= J < N:
                        cur_q.append((I, J))  # error, count multiple times
                        cur_P[I][J] += P[i][j] * 1 / 8

            q = cur_q
            P = cur_P

        return sum([
            P[i][j]
            for i in range(N)
            for j in range(N)
        ])


if __name__ == "__main__":
    assert Solution().knightProbability(3, 2, 0, 0)  == 0.0625
    assert Solution().knightProbability(3, 3, 0, 0)  == 0.015625
