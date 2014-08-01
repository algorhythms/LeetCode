__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        """
        if extra space available, hash table
        if not, use the model of Hare and Tortoise

        The hare totally runs: x + ky + m The tortoise totally runs: x + ty + m
        Thus, ky = 2ty + x + m we have (x + m) mod y = 0 We can conclude that if the hare run more x steps,
        it will reach the cycle's starting node.
        """

        # find cycle
        hare = head
        tortoise = head
        flag = False
        while hare and hare.next and tortoise:
            hare = hare.next.next
            tortoise = tortoise.next
            if hare==tortoise:
                flag = True
                break

        # run more x steps
        cur = None
        if flag:
            cur = head
            while cur:
                if cur==tortoise:
                    break
                cur = cur.next
                tortoise = tortoise.next

        return cur