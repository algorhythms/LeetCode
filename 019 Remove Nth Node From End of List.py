"""
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        O(n)+O(n)
        :param head: head node
        :param n: the nth node from the end
        :return: ListNode, head node
        """
        # construct dummy
        dummy = ListNode(0)
        dummy.next = head

        # get length of the linked list
        length = 0
        pre = dummy
        while pre.next:
            length += 1
            pre=pre.next

        # find & remove
        pre = dummy
        count = 0
        while pre.next:
            cur = pre.next
            if count==length-n:
                pre.next = cur.next  # remove
                break
            else:
                count += 1
                pre = pre.next

        return dummy.next


