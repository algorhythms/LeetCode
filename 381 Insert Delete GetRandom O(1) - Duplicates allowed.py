"""
Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned
is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
"""
from collections import defaultdict
import random

__author__ = 'Daniel'


class RandomizedCollection(object):
    def __init__(self):
        """
        pop set is O(1), deterministic depends on hash value
        Initialize your data structure here.
        """
        self.lst = []
        self.pos = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = True if not self.pos[val] else False

        self.lst.append(val)
        self.pos[val].add(len(self.lst) - 1)

        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.pos[val]:
            return False

        idx, last = self.pos[val].pop(), len(self.lst) - 1
        if idx != last:
            self.lst[idx], self.lst[last] = self.lst[last], self.lst[idx]
            self.pos[self.lst[idx]].remove(last)
            self.pos[self.lst[idx]].add(idx)

        self.lst.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.lst)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()