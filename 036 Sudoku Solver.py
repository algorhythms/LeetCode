"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
"""
__author__ = 'Danyang'
class Solution:
    def solveSudoku(self, board):
        """
        Solve the Sudoku by modifying the input board in-place.

        NP question: N-Queens, Combination Sum, Combinations, Permutations

        :param board: a 9x9 2D array
        :return: NIL
        """
        # break board
        for row in xrange(len(board)):
            board[row] = list(board[row])
        self.solve(board, 0, 0)
        for row in xrange(len(board)):
            board[row] = "".join(board[row])

    def solve_TLE(self, board):
        """

        :param board: a 9x9 2D array
        :return: Boolean
        """
        n = len(board)
        if all([board[i/n][i%n]!="." for i in xrange(n*n)]):
            return True

        for i in xrange(n):
            for j in xrange(n):
                if board[i][j]==".":
                    for num in range(1, 10):
                        num_str = str(num)
                        # row
                        condition_row = all([board[i][col]!=num_str for col in xrange(n)])
                        # col
                        condition_col = all([board[row][j]!=num_str for row in xrange(n)])
                        # square
                        condition_square = all([board[i/3*3+count/3][j/3*3+count%3]!=num_str for count in xrange(n)])

                        if condition_col and condition_row and condition_square:
                            board[i][j] = num_str
                            if not self.solve(board):
                                board[i][j] = "."
                            else:
                                return True

        return False

    def solve(self, board, i, j):
        """
        dfs
        :param board: a 9x9 2D array
        :return: Boolean
        """
        if j>=9:
            return self.solve(board, i+1, 0)
        if i==9:
            return True

        if board[i][j]==".":
            for num in range(1, 10):
                num_str = str(num)  # try number
                # To speed up, use condition short-curcit.
                # row, col, square
                if all([board[i][col]!=num_str for col in xrange(9)]) and \
                        all([board[row][j]!=num_str for row in xrange(9)]) and \
                        all([board[i/3*3+count/3][j/3*3+count%3]!=num_str for count in xrange(9)]):
                    board[i][j] = num_str
                    if not self.solve(board, i, j+1):
                        board[i][j] = "."  # restore, backtrack, save space
                    else:
                        return True
        else:
            return self.solve(board, i, j+1)

        return False

if __name__=="__main__":
    Solution().solveSudoku(
        ["..9748...", "7........", ".2.1.9...", "..7...24.", ".64.1.59.", ".98...3..", "...8.3.2.", "........6",
         "...2759.."]
    )