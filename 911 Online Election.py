#!/usr/bin/python3
"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function:
TopVotedCandidate.q(int t) will return the number of the person that was leading
the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the
most recent vote (among tied candidates) wins.

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],
[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the
most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""
from typing import List
from collections import defaultdict
import bisect


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        """
        Running top vote
        Need to maintain list

        but time is too large to enumerate. Cannot have direct access, then
        query is binary search
        """
        self.maxes = []  # [(t, i)]  at time t
        counter = defaultdict(int)
        tp = sorted(zip(times, persons))
        for t, p in tp:
            counter[p] += 1
            if not self.maxes or counter[self.maxes[-1][1]] <= counter[p]:
                self.maxes.append((t, p))

    def q(self, t: int) -> int:
        i = bisect.bisect(self.maxes, (t, 0))
        # equal
        if i < len(self.maxes) and self.maxes[i][0] == t:
            return self.maxes[i][1]

        # smaller
        i -= 1
        return self.maxes[i][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
