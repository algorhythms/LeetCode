#!/usr/bin/python3
"""
In a country popular for train travel, you have planned some train travelling
one year in advance.  The days of the year that you will travel is given as an
array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get
a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and
8.

Return the minimum number of dollars you need to travel every day in the given
list of days.

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation:
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.

Note:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Iterate backward.

        Why does iterate backward work? Currrent min depends on the future mins

        Let F[i] be the min cost at day i, covering all trips from i to 365
        F[i] = min(F[i + d] + c for d, c in zip([1, 7, 30], costs))
        If day i is not travel day, then wait until i + k that is a travel day

        O(365)
        """
        F = [float("inf") for _ in range(366 + 30)]
        for i in range(366, 366 + 30):
            F[i] = 0

        days_set = set(days)
        for i in range(365, 0, -1):
            if i not in days_set:
                F[i] = F[i+1]
            else:
                F[i] = min(
                    c + F[i+d]
                    for d, c in zip([1, 7, 30], costs)
                )

        return F[1]

    def mincostTickets_error(self, days: List[int], costs: List[int]) -> int:
        """
        Iterate backward on days
        O(30 * |days|)

        Iterate throughout the year is more elegant
        Need buffer day
        """
        n = len(days)
        F = [float("inf") for _ in range(n)]
        F[-1] = costs[0]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                delta = days[j] - days[i]
                if delta <= 1:
                    F[i] = min(F[i], costs[0] + F[j])
                if delta <= 7:
                    F[i] = min(F[i], costs[1] + F[j])
                if delta <= 30:
                    F[i] = min(F[i], costs[2] + F[j])
                else:
                    break
        return F[0]

    def mincostTickets_error(self, days: List[int], costs: List[int]) -> int:
        """
        dp
        Let F[i] be the min cost at day i, covering all trips from day 1 to i
        For 30-day ticiekt, iterate forward all 30 days?
        How to express idle date? Same as previous.

        Why does iterate forward fail? Because future min does not depends on the
        current min. Current higher cost may contribtue to future lower cost.
        """
        F = [float("inf") for _ in range(365 + 1)]
        F[0] = 0
        days_set = set(days)
        for i in range(1, 366):
            if i not in days_set:
                F[i] = F[i-1]
            else:
                # iterate forward does not work
                F[i] = min(F[i], F[i-1] + costs[0])


if __name__ == "__main__":
    assert Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
