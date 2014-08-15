__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        Linked List
        :param head: ListNode
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = pre.next.next

            # temp = node2.next
            # pre.next = node2
            # node2.next = node1
            # node1.next = temp

            pre.next, node1.next, node2.next = node2, node2.next, node1

            pre = pre.next.next

        return dummy.next