#!/usr/bin/python3
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None, None


class LRUCache:

    def __init__(self, capacity: int):
        """
        O(1) look up - Map
        O(1) update most recent vs. least recent - Linked List
        But Single linked list is not enough then Double Linked List

        Need dummy head and tail to avoid over complication of null checking

        Essentially it is the OrderedDict
        """
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._remove(key)
            self._appendleft(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(key)
        elif len(self.map) >= self.cap:
            node = self.tail.prev
            self._remove(node.key)

        node = Node(key, value)
        self._appendleft(node)

    def _appendleft(self, node: Node):
        self.map[node.key] = node  # update/delete map in these two operators
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def _remove(self, key: int):
        node = self.map[key]
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del self.map[key]  # update/delete map in these two operators

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
