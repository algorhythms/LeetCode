"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseKGroup(self, head, k):
        """
        List
        O(k*n)
        :param head: a ListNode
        :param k: an integer
        :return: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur_lst = self.generate_lst(pre.next, k)
        while pre and not None in cur_lst:

            # reverse
            temp = cur_lst[-1].next
            pre.next = cur_lst[-1]
            for i in reversed(xrange(k)):
                if i==0:
                    cur_lst[i].next = temp
                else:
                    cur_lst[i].next = cur_lst[i-1]

            pre = cur_lst[0]
            cur_lst = self.generate_lst(pre.next, k)

        return dummy.next

    def generate_lst(self, node, k):
        """
        Helpder
        :param node: ListNode
        :param k: integer
        :return: list
        """
        lst = []
        cur = node
        for i in xrange(k):
            if cur:
                lst.append(cur)
                cur = cur.next
            else:
                lst.append(None)
        return lst




