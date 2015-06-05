"""
Reverse a singly linked list.
"""
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next
        while pre and cur:
            pre, cur.next, cur = cur, pre, cur.next

        dummy.next.next = None  # original head
        return pre  # new head
