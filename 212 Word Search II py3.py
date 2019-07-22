#!/usr/bin/python3
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""
from typing import List
from collections import defaultdict


dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = defaultdict(TrieNode)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.construct(words)
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        ret = set()
        for i in range(m):
            for j in range(n):
                self.dfs(board, visited, i, j, root, ret)

        return list(ret)

    def dfs(self, board, visited, i, j, cur, ret):
        m, n = len(board), len(board[0])
        visited[i][j] = True
        c = board[i][j]
        if c in cur.children:
            nxt = cur.children[c]
            if nxt.word is not None:
                ret.add(nxt.word)

            for di, dj in dirs:
                I = i + di
                J = j + dj
                if 0 <= I < m and 0 <= J < n and not visited[I][J]:
                    self.dfs(board, visited, I, J, nxt, ret)

        visited[i][j] = False

    def construct(self, words):
        root = TrieNode()
        for w in words:
            cur = root
            for c in w:
                cur = cur.children[c]
            cur.word = w

        return root
