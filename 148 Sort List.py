__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        """
        Workaround by sorted()
        """
        if head==None:
            return None
        lst = [] # must be constant space
        current = head
        while(current):
            lst.append(current)
            current = current.next


        comparator = lambda x, y: cmp(x.val, y.val)
        lst = sorted(lst, comparator)  # return # sorted is not side-effect # O(n log n)
        for i in range(len(lst)-1):
            lst[i].next = lst[i+1]
        lst[-1].next = None
        return lst[0]



