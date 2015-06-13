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
__author__ = 'Daniel'


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.word = None
        self.children = {}  # map from char to TrieNode

    def __repr__(self):
        return repr(self.char)


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def add(self, word):
        word = word.lower()
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.word = word


class Solution:
    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def findWords(self, board, words):
        """
        Trie+dfs
        pure Trie solution

        :param board: a list of lists of 1 length string
        :param words: a list of string
        :return: a list of string
        """
        trie = Trie()
        for word in words:
            trie.add(word)

        ret = set()
        marked = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, trie.root, marked, ret)

        return list(ret)

    def dfs(self, board, i, j, parent, marked, ret):
        """
        :type parent: TrieNode
        """
        m = len(board)
        n = len(board[0])
        marked.add((i, j))
        c = board[i][j]

        if c in parent.children:
            cur = parent.children[c]
            if cur.word:
                ret.add(cur.word)
            for dir in self.dirs:
                row = i+dir[0]
                col = j+dir[1]
                if 0 <= row < m and 0 <= col < n and (row, col) not in marked:
                    self.dfs(board, row, col, cur, marked, ret)

        marked.remove((i, j))