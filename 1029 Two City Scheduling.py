#!/usr/bin/python3
"""
There are 2N people a company is planning to interview. The cost of flying the
i-th person to city A is costs[i][0], and the cost of flying the i-th person to
city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people
arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
interviewing in each city.

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        sort by city A and greedy? [30, 20]?
        sort by total?
        sort by diff - either choose A or B, the difference matters

        a - b: incremental cost of flying A instead of B
        """
        A = [(a - b, a, b) for a, b in costs]
        A.sort()
        ret = 0
        remain = len(A) // 2
        for _, a, b in A:
            if remain > 0:
                ret += a
                remain -= 1
            else:
                ret += b

        return ret

    def twoCitySchedCost_error(self, costs: List[List[int]]) -> int:
        """
        sort by city A and greedy? [30, 20]?
        sort by total?
        sort by diff - either choose A or B, the difference matters

        Error in the abs of difference
        """
        A = [(abs(a - b), a, b) for a, b in costs]
        A.sort(reverse=True)
        ret = 0
        remain = len(A) // 2
        for _, a, b in A:
            if a > b:
                ret += b
            elif remain > 0:
                ret += a
                remain -= 1
            else:
                ret += b

        return ret
