#!/usr/bin/python3
"""
You are standing at position 0 on an infinite number line. There is a goal at
position target.

On each move, you can either go left or right. During the n-th move (starting
from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        """
        math

        put -/+ for 1, 2, 3, 4, ..., k
        flip a sign change in even number

        if target negative, flip the sign. Thus, we can only consider positive
        number
        """
        target = abs(target)
        s = 0
        k = 0
        while s < target:
            k += 1
            s += k

        delta = s - target
        if delta % 2 == 0:
            return k
        else:  # delta is odd
            if (k + 1) % 2 == 1:
                return k + 1
            else:
                return k + 2
