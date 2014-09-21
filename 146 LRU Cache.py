"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it
should invalidate the least recently used item before inserting a new item.
"""
__author__ = 'Danyang'
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = []  # order by key
        self.dic = {}

    def get(self, key):
        if key in self.dic:
            self.q.remove(key)
            self.q.insert(0, key)
            return self.dic[key]
        else:
            return -1

    def set(self, key, value):
        """
        Algorithm:
        data structure: Queue and HashMap

        :param key: int
        :param value: int
        :return: value
        """
        if key in self.dic:
            self.q.remove(key)
            self.q.insert(0, key)
        else:
            if len(self.q)+1<=self.capacity:
                self.q.insert(0, key)
            else:
                self.dic.pop(self.q.pop())
                self.q.insert(0, key)

        self.dic[key] = value
