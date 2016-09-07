"""
Premium Question
"""
__author__ = 'Daniel'


class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0 for _ in xrange(n)]
        self.cols = [0 for _ in xrange(n)]
        self.diag0 = 0
        self.diag1 = 0

    def move(self, row, col, player):
        """
        Since guarantee the move is valid, only store row, col, diagonal.
        1: -1
        2: +1
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        delta = -1 if player == 1 else 1
        self.cols[col] += delta
        self.rows[row] += delta
        if col == row:
            self.diag0 += delta
        if col + row == self.n - 1:
            self.diag1 += delta

        is_win = lambda x: delta * x == self.n
        if any(map(is_win, [self.rows[row], self.cols[col], self.diag0, self.diag1])):
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)