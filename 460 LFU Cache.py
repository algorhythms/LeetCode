#!/usr/bin/python3
"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
from collections import defaultdict, OrderedDict
DUMMY = None


class LFUCache:

    def __init__(self, capacity: int):
        """
        Need priority queue (pq) to keep contract of frequency

        LRU: doubly linked list and map
        Sift up and sift down?

        Ordereded Dict
        map: key -> value
        map: key -> frequency
        map: frequency -> OrderededDict[keys]

        min count is +1
        """
        self.cap = capacity
        self.values = {}
        self.freqs = defaultdict(int)
        self.keys = defaultdict(OrderedDict)
        self.mini = -1  # mini frequency

    def get(self, key: int) -> int:
        if key in self.values:
            val = self.values[key]
            freq_org = self.freqs[key]
            self.freqs[key] += 1
            del self.keys[freq_org][key]
            self.keys[freq_org + 1][key] = DUMMY  # dummy

            if freq_org == self.mini and len(self.keys[self.mini]) == 0:
                self.mini = freq_org + 1

            return val
        else:
            return - 1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:  # trivial
            return

        if key in self.values:
            self.values[key] = value
            self.get(key)  # update
        else:
            if len(self.values) >= self.cap:
                evit_key, _ = self.keys[self.mini].popitem(last=False)  # least recent is at head
                del self.values[evit_key]
                del self.freqs[evit_key]

            self.values[key] = value
            self.freqs[key] = 0
            self.keys[0][key] = DUMMY
            self.get(key)  # update
            self.mini = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
