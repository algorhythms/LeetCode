"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of
the first two lists.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

    def __str__(self):
        return "%d, %s"%(self.val, self.next)

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        Linked List
        assuming ascending order
        :param l1: ListNode
        :param l2: ListNode
        :return:
        """
        dummy = ListNode(0)
        dummy.next = l1

        pre = dummy
        the_other = l2
        while pre and pre.next:
            cur = pre.next
            if the_other and cur.val>the_other.val:
                # insert
                temp = the_other.next
                pre.next, the_other.next = the_other, cur

                the_other = temp  # advance the_other
            pre = pre.next


        # dangling list
        if the_other:
            pre.next = the_other  # appending

        return dummy.next

if __name__=="__main__":
    length = 10
    list1 = [ListNode(2*i) for i in xrange(length)]
    list2 = [ListNode(2*i+1) for i in xrange(length)]
    for i in xrange(length-1):
        list1[i].next = list1[i+1]
        list2[i].next = list2[i+1]

    lst = Solution().mergeTwoLists(list1[0], list2[0])
    print lst
