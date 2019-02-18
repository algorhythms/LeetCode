#!/usr/bin/python3
"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string
represents the key and the integer represents the value. If the key already
existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you
need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.

        Trie

        update using delta
        """
        from collections import defaultdict

        class TrieNode:
            def __init__(self, chr, sum, val):
                self.chr = chr
                self.sum = sum
                self.val = val
                self.children = defaultdict(lambda: None)

        class Trie:
            def __init__(self):
                self.root = TrieNode(None, 0, 0)  # dummy root

            def insert(self, cur, key, i, val):
                if not cur:
                    cur = TrieNode(key[i], 0, 0)

                if i == len(key) - 1:
                    delta = val - cur.val
                    cur.val = val
                else:
                    cur.children[key[i+1]], delta = self.insert(cur.children[key[i+1]], key, i + 1, val)

                cur.sum += delta
                return cur, delta

        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        root = self.trie.root
        root.children[key[0]], _ = self.trie.insert(root.children[key[0]], key, 0, val)

    def sum(self, prefix: str) -> int:
        node = self.trie.root
        for a in prefix:
            if a not in node.children:
                return 0

            node = node.children[a]

        return node.sum


class MapSum2:

    def __init__(self):
        """
        Initialize your data structure here.

        Trie

        update using delta
        """
        class TrieNode:
            def __init__(self, chr, sum, val):
                self.chr = chr
                self.sum = sum
                self.val = val
                self.children = {}

        class Trie:
            def __init__(self):
                self.root = TrieNode(None, 0, 0)  # dummy root

            def insert(self, pi, key, i, val):
                if key[i] not in pi.children:
                    cur = TrieNode(key[i], 0, 0)
                    pi.children[key[i]] = cur

                cur = pi.children[key[i]]
                if i + 1 < len(key):
                    cur.children[key[i+1]], delta = self.insert(cur, key, i + 1, val)
                else:
                    delta = val - cur.val
                    cur.val = val

                cur.sum += delta
                return cur, delta

        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(self.trie.root, key, 0, val)

    def sum(self, prefix: str) -> int:
        node = self.trie.root
        for a in prefix:
            if a not in node.children:
                return 0

            node = node.children[a]

        return node.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
