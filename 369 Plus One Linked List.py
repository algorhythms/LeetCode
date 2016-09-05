"""
Premium question
"""
__author__ = 'Daniel'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def plusOne(self, head):
        """
        reverse, plus one, then reverse
        :type head: ListNode
        :rtype: ListNode
        """
        head = self.revserse(head)
        head = self.plus(head)
        head = self.revserse(head)
        return head

    def plus(self, head):
        cur = head
        while cur:
            cur.val += 1
            if cur.val >= 10:
                cur.val -= 10
                if not cur.next:
                    cur.next = ListNode(0)
                cur = cur.next
            else:
                break

        return head

    def revserse(self, head):
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = pre.next
        while pre and cur:
            nxt = cur.next

            cur.next = pre

            pre = cur
            cur = nxt

        dummy.next.next = None  # original head
        return pre
