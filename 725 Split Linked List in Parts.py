#!/usr/bin/python3
"""
Given a (singly) linked list with head node root, write a function to split the
linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have
a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts
occurring earlier should always have a size greater than or equal parts
occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2,
root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode
is [].

Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import math


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        """
        calculate the chunk/page size at a time

        [1,2,3,4,5,6,7]
        3

        [[1,2,3],[4,5,6],[7]]  # output
        [[1,2,3],[4,5],[6,7]]  # expected
        """
        l = 0
        node = root
        while node:
            l += 1
            node = node.next


        ret = [[] for _ in range(k)]

        short_chunk_l = l // k
        long_chunk_l = short_chunk_l + 1
        n_long_chunk = l % k  # key
        n_short_chunk = l - n_long_chunk

        chunk_counter = 0
        cur_l = 0
        node = root
        while node:
            ret[chunk_counter].append(node.val)
            cur_l += 1
            chunk_size = long_chunk_l if chunk_counter < n_long_chunk else short_chunk_l
            if cur_l == chunk_size:
                cur_l = 0
                chunk_counter += 1
            node = node.next

        return ret

    def splitListToParts_2(self, root: ListNode, k: int) -> List[ListNode]:
        """
        [1,2,3,4,5,6,7]
        3

        [[1,2,3],[4,5,6],[7]]  # output
        [[1,2,3],[4,5],[6,7]]  # expected

        need to dynamical calculate part length on the fly
        """
        l = 0
        node = root
        while node:
            l += 1
            node = node.next


        ret = [[] for _ in range(k)]
        node = root
        counter = 0
        cur_l = 0
        i = 0
        part_l = math.ceil((l - counter) / k)
        while node:
            cur_l += 1
            counter += 1
            ret[i].append(node.val)
            if cur_l == part_l:
                k -= 1
                cur_l = 0
                i += 1
                if k != 0:
                    part_l = math.ceil((l - counter) / k)

            node = node.next

        return ret

    def splitListToParts_error(self, root: ListNode, k: int) -> List[ListNode]:
        """
        mistake, the length should be dynamically calculated

        [1,2,3,4,5,6,7]
        3

        [[1,2,3],[4,5,6],[7]]  # output
        [[1,2,3],[4,5],[6,7]]  # expected
        """
        l = 0
        node = root
        while node:
            l += 1
            node = node.next

        part_l = math.ceil(l / k)
        ret = [[] for _ in range(k)]

        node = root
        cur_l = 0
        i = 0
        while node:
            cur_l += 1
            ret[i].append(node.val)
            if cur_l == part_l:
                cur_l = 0
                i += 1

            node = node.next

        return ret
