#!/usr/bin/python3
"""
Given a list of daily temperatures T, return a list such that, for each day in
the input, tells you how many days you would have to wait until a warmer
temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each
temperature will be an integer in the range [30, 100].
"""
from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        maintain a stack of monotonously decresing from right to left
        (i.e. monotonously increasing from left to right)

        Why stack? because you can disregard certain non-usefull information 

        scanning from right
        [73, 74, 75, 71, 69, 72, 76, 73]
        """
        ret = deque()
        stk = []
        for i in range(len(T) - 1, -1 , -1):
            while stk and T[stk[-1]] <= T[i]:  # disregard smaller ones
                stk.pop()

            if stk:
                ret.appendleft(stk[-1] - i)
            else:
                ret.appendleft(0)
            stk.append(i)

        return list(ret)


if __name__ == "__main__":
    assert Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
