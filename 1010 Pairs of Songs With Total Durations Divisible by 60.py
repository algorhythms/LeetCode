#!/usr/bin/python3
"""
In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is
divisible by 60.  Formally, we want the number of indices i < j with (time[i] +
time[j]) % 60 == 0.

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.

Note:
1 <= time.length <= 60000
1 <= time[i] <= 500
"""
from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        Running attribution
        """
        counter = defaultdict(int)
        ret = 0
        for t in time:
            ret += counter[(60 - t) % 60]  # handle 0
            counter[t % 60] += 1

        return ret


    def numPairsDivisibleBy60_error(self, time: List[int]) -> int:
        """
        O(N^2) check i, j
        Reduce it
        O(N) by using hashmap, the key should mod 60

        attribution error
        """
        hm = defaultdict(int)
        for t in time:
            hm[t % 60] += 1

        ret = 0
        for k, v in hm.items():
            if k == 0:
                ret += (v * (v - 1)) // 2
            elif k <= 60 - k:  # attribution
                v2 =  hm[60 - k]
                ret += v2 * v

        return ret
