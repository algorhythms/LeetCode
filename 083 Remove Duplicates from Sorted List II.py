"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the
original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        Two pointers
        :param head: ListNode
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.next and cur.next.val==cur.val:  # duplicated
                # find the next non_duplicate
                next_non_duplicate = cur.next
                while next_non_duplicate and cur.val==next_non_duplicate.val:
                    next_non_duplicate = next_non_duplicate.next

                # remove all duplicated nodes 
                pre.next = next_non_duplicate

            else:
                pre = pre.next

        return dummy.next




