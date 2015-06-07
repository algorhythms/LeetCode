# -*- coding: utf-8 -*-
"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
__author__ = 'Daniel'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        We can do something with the length difference.

        :type headA: ListNode
        :type headB: ListNode
        :rtype: ListNode
        """
        l_a = self._get_len(headA)
        l_b = self._get_len(headB)
        if l_a > l_b:
            l_a, l_b = l_b, l_a
            headA, headB = headB, headA

        cur_a = headA
        cur_b = headB
        for i in xrange(l_b-l_a):
            cur_b = cur_b.next

        while cur_a != cur_b:
            cur_a = cur_a.next
            cur_b = cur_b.next

        return cur_a

    def _get_len(self, head):
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        return n