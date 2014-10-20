"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
__author__ = 'Danyang'
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists_TLE1(self, lists):
        """
        k lists; each list has N items
        Algorithm 1:
        Merge the lists 1 by 1, just add a loop outside the merge.
        Complexity: 2N+3N+4N+..kN = O(k^2 * N)

        Algorithm 2:
        Group the lists in pairs with every pair having 2 lists, merge two, then repeat again
        Complexity:
        T(N) = (k/2)*2N+(k/4)*4N..+(k/2^r)*2^r*N
        T(N) = O(lg k * k * N)

        :param lists: a list of ListNode
        :return: ListNode
        """
        lists = filter(lambda x: x is not None, lists)
        if not lists:
            return

        length = len(lists)
        factor = 2
        while length>0:
            i = 0
            while True:
                try:
                    lists[i] = self.mergeTwoLists(lists[i], lists[i+factor/2])
                except IndexError:
                    break
                i += factor

            length /= 2
            factor *= 2

        return lists[0]

    def mergeKLists_TLE2(self, lists):
        """

        :param lists: a list of ListNode
        :return: ListNode
        """
        lists = filter(lambda x: x is not None, lists)
        if not lists:
            return

        result = lists[0]
        for i in xrange(1, len(lists)):
            result = self.mergeTwoLists(result, lists[i])
        return result



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

    def mergeKLists(self, lists):
        """
        use heap
        heap pointer

        -------------------
         |  |  |  |  |  |
         |  |  |  |  |  |
         |  |  |  |  |  |
         |  |  |  |  |  |

        reference: https://github.com/leetcoders/Leetcode-Py/blob/master/Merge%20k%20Sorted%20Lists.py
        :param lists:
        :return:
        """
        heap = []
        for head_node in lists:
            if head_node:
                heapq.heappush(heap, (head_node.val, head_node))

        dummy = ListNode(0)

        cur = dummy
        while heap:
            smallest_node = heapq.heappop(heap)[1]
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, smallest_node.next))
        return dummy.next

if __name__=="__main__":
    assert  Solution().mergeKLists([None, None])==None
    assert Solution().mergeKLists([ListNode(1), ListNode(0)]).val==0
