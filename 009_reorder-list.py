__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList_TLE(self, head):
        dummy_head = ListNode(0)
        dummy_head.next = head

        pre_cur = dummy_head
        while(pre_cur and pre_cur.next):
            # find last
            pre_last = pre_cur.next
            if pre_last.next == None:
                return
            while(pre_last.next.next):
                pre_last = pre_last.next

            last = pre_last.next

            # shift
            cur = pre_cur.next
            cur_next = cur.next
            if cur_next!= last and cur!= last:
                cur.next = last
                last.next = cur_next
                # fix last
                pre_last.next = None

            if cur_next and cur_next.next==last:
                cur_next.next = None


            pre_cur = pre_cur.next.next

    def reorderList(self, head):
        """
        relies on additional data structure 
        """
        lst = []
        cur = head
        while(cur):
            lst.append(cur)
            cur = cur.next

        lst1 = lst[:len(lst)/2]
        lst2 = lst[len(lst)/2:]
        lst2.reverse()

        lst = []
        for i in range(len(lst2)):
            try:
                lst.append(lst1[i])
            except IndexError:
                pass
            lst.append(lst2[i])

        for i in range(len(lst)):
            try:
                lst[i].next = lst[i+1]
            except IndexError:
                lst[i].next = None






if __name__=="__main__":
    length = 3
    lst = [ListNode(i+1) for i in range(length)]
    for i in range(length-1):
        lst[i].next = lst[i+1]

    Solution().reorderList(lst[0])

    cur = lst[0]
    while(cur):
        print cur.val
        cur = cur.next
