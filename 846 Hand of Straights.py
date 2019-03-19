#!/usr/bin/python3
"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W,
and consists of W consecutive cards.

Return true if and only if she can.



Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.


Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""
from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def isNStraightHand(self, A: List[int], W: int) -> bool:
        """
        sort + queue

        prev = previous value
        prev_cnt = previous value count
        """
        q = deque()
        counter = Counter(A)
        prev = 0
        prev_cnt = 0
        for k in sorted(counter):  # sorted by key
            if prev_cnt > counter[k] or prev_cnt > 0 and k > prev + 1:
                return False
                
            q.append(counter[k] - prev_cnt)
            prev, prev_cnt = k, counter[k]
            if len(q) == W:
                c = q.popleft()
                prev_cnt -= c

        return prev_cnt == 0

    def isNStraightHand_heap(self, A: List[int], W: int) -> bool:
        """
        sort + heap
        O(N log N + N log N)
        """
        A.sort()
        if len(A) % W != 0:
            return False
        if W == 1:
            return True


        h = []  # tuple of (-3, [1, 2, 3])
        for a in A:
            if not h:
                h = [(a, [a])]
                continue

            if a == h[0][1][-1]:
                heapq.heappush(h, (a, [a]))
            elif a == h[0][1][-1] + 1:
                _, lst = heapq.heappop(h)
                lst.append(a)
                if len(lst) < W:
                    heapq.heappush(h, (a, lst))
            else:
                return False

        if h:
            return False

        return True


if __name__ == "__main__":
    assert Solution().isNStraightHand([1,2,3,6,2,3,4,7,8], 3) == True
    assert Solution().isNStraightHand([1,1,2,2,3,3], 3) == True
