#!/usr/bin/python3
"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign
represents its direction (positive meaning right, negative meaning left). Each
asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet,
the smaller one will explode. If both are the same size, both will explode. Two
asteroids moving in the same direction will never meet.

Example 1:
Input:
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input:
asteroids = [8, -8]
Output: []
Explanation:
The 8 and -8 collide exploding each other.
Example 3:
Input:
asteroids = [10, 2, -5]
Output: [10]
Explanation:
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input:
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation:
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each
other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        simplified

        while-else: break statement break the entire while-else block
        for-else: break statement break the entire for-else block

        stack from left to right, only -> <- will pop the stack
        """
        stk = []
        for e in asteroids:
            while stk and e < 0 < stk[-1]:
                if abs(e) > abs(stk[-1]):
                    # -> exploded, <- continues
                    stk.pop()
                elif abs(e) == abs(stk[-1]):
                    # -> <- both exploded
                    stk.pop()
                    break
                else:
                    # <- exploded, -> continue
                    break
            else:
                stk.append(e)

        return stk

    def asteroidCollision_complex(self, asteroids: List[int]) -> List[int]:
        """
        asteroids same speed
        list of size

        stk of index

        only -> <- will collide
        """
        stk = []
        n = len(asteroids)
        for i in range(n-1, -1, -1):
            cur = asteroids[i]
            while stk and asteroids[stk[-1]] < 0 and cur > 0 and abs(asteroids[stk[-1]]) < abs(cur):
                stk.pop()

            if stk and cur > 0 and asteroids[stk[-1]] == -cur:
                stk.pop()
                continue

            if not stk:
                stk.append(i)
                continue

            if not (asteroids[stk[-1]] < 0 and cur > 0) or abs(cur) > abs(asteroids[stk[-1]]):
                stk.append(i)

        return [
            asteroids[i]
            for i in stk[::-1]
        ]


if __name__ == "__main__":
    assert Solution().asteroidCollision([10, 2, -5]) == [10]
    assert Solution().asteroidCollision([5, 10, -5]) == [5, 10]
    assert Solution().asteroidCollision([8, -8]) == []
