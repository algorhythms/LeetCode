__author__ = 'Danyang'
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        # for debugger
        return repr(self.val)

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        """
        Two pointers & math
        :param l1: linked list head node
        :param l2: linked list head node
        :return: head node
        """
        result_head = ListNode(0)

        cur1 = l1
        cur2 = l2
        cur = result_head
        while cur1 or cur2:
            cur.val += self.addNode(cur1, cur2)
            if cur.val<10:
                if cur1 and cur1.next or cur2 and cur2.next:  # next node
                    cur.next = ListNode(0)
            else:
                cur.val -= 10
                cur.next = ListNode(1)

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next
            cur = cur.next

        return result_head

    def addNode(self, node1, node2):
        if not node1 and not node2:
            raise Exception("two nodes are None")
        if not node1:
            return node2.val
        if not node2:
            return node1.val
        return node1.val + node2.val

if __name__=="__main__":
    l1s = [ListNode(1)]
    l2s = [ListNode(9), ListNode(9)]
    for i in range(len(l1s)-1):
        l1s[i].next = l1s[i+1]
    for i in range(len(l2s)-1):
        l2s[i].next = l2s[i+1]
    Solution().addTwoNumbers(l1s[0], l2s[0])
