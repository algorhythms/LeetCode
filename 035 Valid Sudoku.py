"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""
__author__ = 'Danyang'
class Solution:
    def isValidSudoku(self, board):
        """
        Brute force - check rows, cols, and squares and maintain a hashmap to store the previously seen elements

        Notice how check the square in the board.

        Save space by one iterations.

        9 squares are iterated by i
        9 cells are iterated by j
        Squares lie on 3 big rows; index for the 3 big rows: i/3*3-th, thus iteration pattern: 000, 333, 666
        Subdivide the 1 big rows into 3 small rows; index for the 3 small rows: j/3-th, thus iteration pattern 000, 111, 222)

        Squares lie on 3 big column; index for the 3 big column: i%3*3-th, thus iteration pattern: (036, 036, 036)
        Subdivide the 1 big column into 3 small column; index for the 3 small columns: j%3-th, thus iteration pattern 012, 012, 012)

        thus, iterate by board[i/3*3 + j/3][i%3*3 + j%3]

        :param board: a 9x9 2D array
        :return: boolean
        """
        # check row & column
        for i in xrange(9):
            row = []  # change to hashamp
            column = []
            square = []
            for j in xrange(9):
                # check row
                try:
                    row_element = int(board[i][j])
                    if row_element in row:
                        return False
                    else:
                        row.append(row_element)
                except ValueError:
                    pass

                # check column
                try:
                    column_element = int(board[j][i])
                    if column_element in column:
                        return False
                    else:
                        column.append(column_element)
                except ValueError:
                    pass

                # check square
                try:
                    square_element = int(board[i/3*3 + j/3][i%3*3 + j%3])
                    if square_element in square:
                        return False
                    else:
                        square.append(square_element)
                except ValueError:
                    pass

        return True

if __name__=="__main__":
    assert Solution().isValidSudoku(
        ["..4...63.", ".........", "5......9.", "...56....", "4.3.....1", "...7.....", "...5.....", ".........",
         "........."]
    )==False
