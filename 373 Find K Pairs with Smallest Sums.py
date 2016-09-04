"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""
import heapq

__author__ = 'Daniel'


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        Maintain a heap of the k pairs
        The art is how to select the next pair.

        O(k log k)

        https://discuss.leetcode.com/topic/50885/simple-java-o-klogk-solution-with-explanation
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        class Node(object):
            def __init__(self, i, j):
                self.i, self.j = i, j

            def __cmp__(self, other):
                return nums1[self.i] + nums2[self.j] - (nums1[other.i] + nums2[other.j])

            def hasnext(self):
                return self.j + 1 < len(nums2)

            def next(self):
                if self.hasnext():
                    return Node(self.i, self.j + 1)

                raise StopIteration

        if not nums1 or not nums2:
            return []

        h = []
        for i in xrange(min(k, len(nums1))):
            heapq.heappush(h, Node(i, 0))

        ret = []
        while h and len(ret) < k:
            node = heapq.heappop(h)
            ret.append([nums1[node.i], nums2[node.j]])
            if node.hasnext():
                heapq.heappush(h, node.next())

        return ret

    def kSmallestPairsError(self, nums1, nums2, k):
        """
        The merge process for merge sort
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        ret = []
        for _ in xrange(k):
            if i < len(nums1) and j < len(nums2):
                ret.append([nums1[i], nums2[j]])
                if nums1[i] < nums2[j]:
                    j += 1
                else:
                    i += 1
            else:
                break

        return ret


if __name__ == "__main__":
    assert Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 9) == [[1, 2], [1, 4], [1, 6], [7, 2], [7, 4], [11, 2],
                                                                   [7, 6], [11, 4], [11, 6]]