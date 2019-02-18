#!/usr/bin/python3
"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to
build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify
exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
"""
from typing import List
from collections import defaultdict


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        class Node:
            def __init__(self, chr):
                self.chr = chr
                self.end = False  # a word ends here
                self.children = defaultdict(lambda: None)

        class Trie:
            def __init__(self):
                self.root = Node(None)

            def insert(self, cur, s, i):
                if not cur:
                    cur = Node(s[i])

                if i == len(s) -1:
                    cur.end = True
                else:
                    nxt = s[i+1]
                    cur.children[nxt] = self.insert(cur.children[nxt], s, i + 1)

                return cur

            def search(self, cur, s, i, modified):
                if cur.chr != s[i]:
                    if modified:
                        return False
                    modified = True

                if i == len(s) - 1:
                    # modified exactly once and have a word ends here 
                    return modified and cur.end

                for child in cur.children.values():
                    if self.search(child, s, i + 1, modified):
                        return True

                return False

        self.trie = Trie()

    def buildDict(self, dic: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for s in dic:
            root = self.trie.root
            root.children[s[0]] = self.trie.insert(root.children[s[0]], s, 0)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for child in self.trie.root.children.values():
            if self.trie.search(child, word, 0, False):
                return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
