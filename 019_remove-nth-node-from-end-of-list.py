__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        """
        Given a linked list, remove the nth node from the end of list and return its head.
        :param head: head node
        :param n: the nth node from the end
        :return: head node
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
                pre.next = cur.next
                break
            else:
                count += 1
                pre = pre.next

        return dummy.next


