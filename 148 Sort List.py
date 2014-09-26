"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def sortList_array(self, head):
        """
        Workaround by sorted()
        :param head: ListNode
        :return: ListNode
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

    def sortList(self, head):
        """
        Quick sort: not guarantee to be O(n lgn)
        Heap sort: not great as index
        Merge sort: H(n) = 2H(n/2) + n/2, thus O(n lgn)

        :param head: ListNode
        :return: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        slow_pre = dummy
        fast_pre = dummy
        while fast_pre.next and fast_pre.next.next:
            fast_pre = fast_pre.next.next
            slow_pre = slow_pre.next

        mid_head = slow_pre.next
        dummy_mid = ListNode(0)

        # sort sub-problem
        slow_pre.next = None  # break
        head = self.sortList(head)
        mid_head = self.sortList(mid_head)

        # then merge
        dummy.next = head
        dummy_mid.next = mid_head
        pre = dummy
        pre_mid = dummy_mid
        while pre.next and pre_mid.next:
            if pre.next.val > pre_mid.next.val:
                pre.next, pre_mid.next.next, pre_mid.next = pre_mid.next, pre.next, pre_mid.next.next
                pre = pre.next
            else:
                pre = pre.next

        # dangling
        if  pre_mid.next:
            pre.next = pre_mid.next

        return dummy.next




if __name__=="__main__":
    length = 5
    lst = [ListNode(length-i) for i in range(length)]
    for i in range(length-1):
        lst[i].next = lst[i+1]

    head = Solution().sortList(lst[0])

    cur = head
    while(cur):
        print cur.val
        cur = cur.next