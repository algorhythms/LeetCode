#!/usr/bin/python3
"""
Implement a MyCalendar class to store your events. A new event can be added if
adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this
represents a booking on the half open interval [start, end), the range of real
numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie.,
there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be
added to the calendar successfully without causing a double booking. Otherwise,
return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar();
MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already
booked by another event.
The third event can be booked, as the first event takes every time less than 20,
but not including 20.


Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range
[0, 10^9].
"""


class Node:
    def __init__(self, s, e):
        self.s = s
        self.e = e
        self.left = None
        self.right = None


class MyCalendar:
    def __init__(self):
        """
        binary search
        disregard
        end < new.start
        start > new.end
        need to find
        end > new.start
        start < new.end

        keep sorted, list insert O(n)
        need a TreeMap
        but python does not have -> BST although unbalanced
        """
        self.root = None

    def insert(self, node: Node, s: int, e: int) -> Node:
        if not node:
            return Node(s, e)

        if e <= node.s:
            left = self.insert(node.left, s, e)
            if left is None:
                return None
            node.left = left
            return node
        elif s >= node.e:
            right = self.insert(node.right, s, e)
            if right is None:
                return None
            node.right = right
            return node
        else:
            return None

    def book(self, start: int, end: int) -> bool:
        ret = self.insert(self.root, start, end)
        if ret is None:
            return False

        self.root = ret
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
