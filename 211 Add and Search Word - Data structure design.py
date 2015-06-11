"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can
represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
__author__ = 'Daniel'


class TrieNode:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # node value depends on the parent's hash mapping
        self.ended = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one
        letter.
        :type word: str
        :rtype: bool
        """
        return self.__search(word, self.root)

    def __search(self, word, cur):
        if not word:
            return cur.ended

        w = word[0]
        if w != ".":
            if w in cur.children:
                return self.__search(word[1:], cur.children[w])
            else:
                return False
        else:
            for child in cur.children.values():
                if self.__search(word[1:], child):
                    return True

        return False

if __name__ == "__main__":
    dic = WordDictionary()
    dic.addWord("a")
    assert dic.search(".") == True