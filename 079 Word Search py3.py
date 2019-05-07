#!/usr/bin/python3
"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
from typing import List
from collections import defaultdict


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = defaultdict(lambda: defaultdict(bool))
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, visited, i, j, word, 1):
                        return True

        return False

    def dfs(self, board, visited, i, j, word, idx):
        visited[i][j] = True
        if idx >= len(word):
            return True

        m, n = len(board), len(board[0])
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and board[I][J] == word[idx]:
                if self.dfs(board, visited, I, J, word, idx + 1):
                    return True

        visited[i][j] = False  # restore
        return False


if __name__ == "__main__":
    assert Solution().exist([
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
    ], "ABCESEEEFS") == True
