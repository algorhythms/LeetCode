"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """

        :param head:
        :param val:
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
                continue

            pre = pre.next

        return dummy.next