__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def detectCycle(self, head):
        """
        if extra space available, hash table
        if not, use the model of Hare and Tortoise

        The hare totally runs: x + ky + m The tortoise totally runs: x + ty + m
        Thus, ky = 2ty + x + m we have (x + m) mod y = 0 We can conclude that if the hare run more x steps,
        it will reach the cycle's starting node.
        """
        hare = head
        tortoise = head
        while hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare==tortoise:
                pass
        # TODO

