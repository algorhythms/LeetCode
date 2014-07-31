__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        """
        if extra space available, hash table
        if not, use the model of Hare and Tortoise
        """
        hare = head
        tortoise = head
        while hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare==tortoise:
                return True

        return False
