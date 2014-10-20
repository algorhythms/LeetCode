"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
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
        return str(self.val)+", "+str(self.next)

class Solution:
    def reverseBetween(self, head, m, n):
        """
        Linked List
        [m, n)
        :param head: ListNode
        :param m: int
        :param n: int
        :return: ListNode
        """
        # trivial
        if not head or m>=n:
            return head

        dummy = ListNode(0)
        dummy.next = head

        cnt = 1  # position starting from 1
        pre = dummy

        start_pre = None
        start = None

        cur = pre.next  # cannot put it in while loop? affect reverse link
        while pre.next:
            # record starting point
            if cnt==m:
                start_pre = pre
                start = cur

            # reverse link (not node)
            # 1 -> 2 -> 3
            # 1 <- 2 -> 3
            elif m<cnt<=n:
                # temp = cur.next
                # cur.next = pre
                # pre = cur
                # cur = temp

                # cur.nex is assign first, left to right
                cur.next, pre, cur = pre, cur, cur.next  # different from pre, cur, cur.next = cur, cur,next, pre
                cnt += 1
                continue

            # reconnect
            elif cnt==n+1:
                end = pre
                start_pre.next = end
                start.next = cur
                break



            pre = pre.next
            cur = cur.next
            cnt += 1

        return dummy.next

if __name__=="__main__":
    length = 3
    lst = [ListNode(i+1) for i in range(length)]
    for i in xrange(length-1):
        lst[i].next = lst[i+1]
    print Solution().reverseBetween(lst[0], 1, 3)