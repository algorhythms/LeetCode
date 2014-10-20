"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
* note, misrepresentation in the original question
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
__author__ = 'Danyang'
class Solution:
    def exist(self, board, word):
        """
        dfs
        :param board: a list of lists of 1 length string
        :param word: a string
        :return: boolean
        """
        if not board:
            return
        # unpack
        # board = [item[0] for item in board]

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]  # avoid loop
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j]==word[0]:
                    visited[i][j] = True
                    if self.search(board, i, j, word[1:], visited):
                        return True
                    visited[i][j] = False
        return False

    def search(self, board, pre_row, pre_col, word, visited):
        if not word:
            return True
        # searching for word[0]
        m = len(board)
        n = len(board[0])
        next_positions = [(pre_row-1, pre_col), (pre_row+1, pre_col), (pre_row, pre_col-1), (pre_row, pre_col+1)]  # four directions
        for next_position in next_positions:
            if 0<=next_position[0]<m and 0<=next_position[1]<n:  # pre-checking
                if visited[next_position[0]][next_position[1]]==False and board[next_position[0]][next_position[1]]==word[0]:
                    visited[next_position[0]][next_position[1]] = True
                    if self.search(board, next_position[0], next_position[1], word[1:], visited):
                        return True
                    visited[next_position[0]][next_position[1]] = False  # restore
        return False



if __name__=="__main__":
    board = [
        "ABCE",
        "SFCS",
        "ADEE"
    ]
    word = "ABCCED"
    print Solution().exist(board, word)