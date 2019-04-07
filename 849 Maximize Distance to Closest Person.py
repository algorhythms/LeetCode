#!/usr/bin/python3
"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents
that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest
person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has
distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        DP from left and right - next array
        Let L[i] be the distant to the left 1 at A[i]
        Let R[i] ...
        """
        n = len(seats)
        L = [float("inf") for _ in range(n)]
        R = [float("inf") for _ in range(n)]
        for i in range(n):
            if seats[i] == 1:
                L[i] = 0
            elif i - 1 >= 0:
                L[i] = L[i-1] + 1
        for i in range(n-1, -1 , -1):
            if seats[i] == 1:
                R[i] = 0
            elif i + 1 < n:
                R[i] = R[i+1] + 1

        return max(
            min(L[i], R[i])
            for i in range(n)
        )

    def maxDistToClosest2(self, seats: List[int]) -> int:
        """
        maintain a sorrted index array
        """
        idxes = []
        for i, e in enumerate(seats):
            if e == 1:
                idxes.append(i)

        ret = [-float("inf"), 0]
        n = len(seats)
        # two ends
        for i, j in zip((0, n-1), (0, -1)):
            dist = abs(i - idxes[j])
            if dist > ret[0]:
                ret = [dist, i]

        for j in range(len(idxes) - 1):
            i = (idxes[j] + idxes[j+1]) // 2
            dist = min(abs(i - idxes[j]), abs(i - idxes[j+1]))
            if dist > ret[0]:
                ret = [dist, i]

        return ret[0]


if __name__ == "__main__":
    assert Solution().maxDistToClosest([1,0,0,0,1,0,1]) == 2
