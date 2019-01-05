#!/usr/bin/python3
"""
Winter is coming! Your first job during the contest is to design a standard
heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find
out minimum radius of heaters so that all houses could be covered by those
heaters.

So, your input will be the positions of houses and heaters seperately, and your
expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
"""
import bisect


class Solution:
    def findRadius(self, houses, heaters):
        """
        check the responsibility
        use bisect
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        r = 0
        i = 0
        for h in houses:
            i = bisect.bisect(heaters, h)  # insertion point
            left = max(0, i - 1)
            right = min(len(heaters) - 1, i)
            r_cur = min(abs(heaters[left] - h), abs(heaters[right] - h))
            r = max(r, r_cur)
            
        return r

    def findRadius_naive(self, houses, heaters):
        """
        check the responsibility
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters.append(float('inf'))
        r = 0
        i = 0
        for h in houses:
            # possible bisect
            while h > (heaters[i] + heaters[i+1]) / 2:
                # find which heater is responsible for the house
                i += 1

            r = max(r, abs(heaters[i] - h))

        return r


if __name__ == "__main__":
    assert Solution().findRadius([1,2,3,4], [1,4]) == 1
