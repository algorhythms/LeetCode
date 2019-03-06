#!/usr/bin/python3
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        return prev

    def reverseList_complex(self, head: ListNode) -> ListNode:
        if not head:
            return None

        prev = head
        cur = head.next
        head.next = None
        while prev and cur:
            nxt = cur.next
            cur.next = prev

            prev = cur
            cur = nxt

        return prev
