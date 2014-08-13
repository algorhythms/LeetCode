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
        lst = []
        cur = node
        for i in xrange(k):
            if cur:
                lst.append(cur)
                cur = cur.next
            else:
                lst.append(None)
        return lst




