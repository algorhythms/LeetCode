#!/usr/bin/python3
"""
There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.
 

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
Example 2:

Input: a = 4, b = 3, c = 2
Output: [0,0]
Explanation: We cannot make any moves.
Example 3:

Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
 

Constraints:

1 <= a, b, c <= 100
a, b, and c have different values.
"""
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        """
        max: move 1 slot by 1 slot 
        min: move the entire gap. 
        """
        A = [a, b, c]
        A.sort()
        gap_l = A[1] - A[0] - 1
        gap_r = A[2] - A[1] - 1
        maxa = gap_l + gap_r
        
        min_gap = min(gap_l, gap_r)
        if gap_l == 0 and gap_r == 0:
            mini = 0
        elif min_gap == 0 or min_gap == 1:
            mini = 1
        else:
            mini = 2

        return mini, maxa