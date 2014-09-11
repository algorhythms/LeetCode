"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
        Two pointers, closed_ptr and open_ptr, to find the next non-duplicate
        O(n)
        :param head: ListNode
        :return: ListNode
        """
        # trivial
        if not head:
            return head
        # main
        closed_ptr = head
        open_ptr = head.next
        while open_ptr:
            # find the non-duplicate
            while open_ptr and closed_ptr.val==open_ptr.val:
                open_ptr = open_ptr.next

            closed_ptr.next = open_ptr
            closed_ptr = closed_ptr.next
            open_ptr = open_ptr.next if open_ptr else None

        return head

if __name__=="__main__":
    nodes = [ListNode(1) for _ in range(2)]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]

    Solution().deleteDuplicates(nodes[0])