"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of
being returned.
Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 1 is the only number in the set, getRandom always return 1.
randomSet.getRandom();
"""
import random

__author__ = 'Daniel'


class RandomizedSet(object):
    def __init__(self):
        """
        1. Use List of numbers to support O(1) getRandom
        2. need an efficient way to find and delete an element
        3. Use Map to get the location, move to end and pop
        Initialize your data structure here.
        """
        self.lst = []
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False

        self.lst.append(val)
        self.pos[val] = len(self.lst) - 1

        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        idx, last = self.pos[val], len(self.lst) - 1

        if idx != last:
            self.lst[idx], self.lst[last] = self.lst[last], self.lst[idx]
            self.pos[self.lst[idx]] = idx

        del self.pos[val]
        self.lst.pop()

        return True

    def getRandom(self):
        """
        Gets a random element from the set.
        :rtype: int
        """
        return random.choice(self.lst)


class RandomizedSetTLE(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val not in self.set
        self.set.add(val)
        return ret

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        ret = val in self.set
        self.set.discard(val)
        return ret

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.sample(self.set, 1)[0]  # O(N), equivalent to random.choice(tuple(allLetters))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
