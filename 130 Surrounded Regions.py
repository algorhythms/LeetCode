"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
__author__ = 'Danyang'
CONNECTED = 'C'
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def solve(self, board):
        """
        Graph Theory
        Algorithm1: bfs, to tell whether it is on the boarder
        Algorithm2: bfs, to get the connectivity graph
        :param board: a 2D array
        :return: NIL, Capture all regions by modifying the input board in-place.
        """
        if not board or not board[0]:
            return
        q = []
        # scan the boarder
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            if board[i][0]=='O': q.append((i, 0))
            if board[i][n-1]=='O': q.append((i, n-1))
        for j in xrange(1, n-1):
            if board[0][j]=='O': q.append((0, j))
            if board[m-1][j]=='O': q.append((m-1, j))


        while q: # dynamically expanding, no deletion of elements
            cor = q.pop()
            board[cor[0]][cor[1]]=CONNECTED  # cannot be both "O" and CONNECTED
            for direction in directions:
                row = cor[0]+direction[0]
                col = cor[1]+direction[1]
                if 0<=row<m and 0<=col<n and board[row][col]=='O':
                    q.append((row, col))


        for i in xrange(m):
            for j in xrange(n):
                if board[i][j]=='O':
                    board[i][j] = 'X'
                elif board[i][j]==CONNECTED:
                    board[i][j] = 'O'


if __name__=="__main__":
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    expected_board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'X', 'X']
    ]
    Solution().solve(board)
    assert board==expected_board




