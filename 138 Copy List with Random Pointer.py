"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null.

Return a deep copy of the list.
"""
__author__ = 'Danyang'
# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        """
        Algorithm:

        Duplicate the node in the list
        Split the list into two

        A->B->C

        A->A'->B->B'->C->C'

        A->B->C
        A'->B'->C'

        :param head: RandomListNode
        :return: RandomListNode
        """
        # duplicate
        dummy = RandomListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next:
            cur = pre.next
            cur_copy = RandomListNode(cur.label)

            temp = cur.next
            cur.next = cur_copy
            cur_copy.next = temp

            pre = pre.next.next

        # copy random
        pre = dummy
        while pre.next:
            cur = pre.next

            if cur.random:
                cur.next.random = cur.random.next  # for duplicated node. NEXT IS RANDOM

            pre = pre.next.next

        # split
        pre = dummy
        head_copy = pre.next.next if pre.next else None
        while pre.next:
            cur = pre.next
            cur_copy = cur.next

            cur.next = cur_copy.next
            if cur_copy.next:
                cur_copy.next = cur_copy.next.next

            pre = pre.next


        return head_copy