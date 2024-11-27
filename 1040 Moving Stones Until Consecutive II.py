#!/usr/bin/python3
"""
There are some stones in different positions on the X-axis. You are given an integer array stones, the positions of the stones.

Call a stone an endpoint stone if it has the smallest or largest position. In one move, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.

In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.
The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

answer[0] is the minimum number of moves you can play, and
answer[1] is the maximum number of moves you can play.
 

Example 1:

Input: stones = [7,4,9]
Output: [1,2]
Explanation: We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
Example 2:

Input: stones = [6,5,4,3,10]
Output: [2,3]
Explanation: We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.
 

Constraints:

3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
All the values of stones are unique.
"""
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        A = sorted(stones)
        n = len(A)
        # Calculate Max:
        # move every endpoint stone to every hole
        hi = max(
            # move A[0]
            A[~0] - A[1] + 1 - (n - 1),
            # move A[~0]
            A[~1] - A[0] + 1 - (n - 1),
        )

        # Calcualte Min:
        # sliding window 
        lo = n
        i = 0
        for j in range(n):
            while i < j and A[j] - A[i] + 1 > n:
                i += 1
            
            total_slots = A[j] - A[i] + 1
            existing = j - i + 1
            
            if total_slots == n - 1 and existing == n - 1:
                # edge case: [1, 2, 3, 10]
                lo = min(lo, 2)
            else:
                # move stones outside the window into it or adjacent to it
                lo = min(lo, n - existing)
        
        return lo, hi


from collections import deque


class SolutionWrongTLE:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        """
        calculate gap array 
        max = sum(gaps)? Has to move it s.t. no longer endpoint 
        greedy, move to max / min gap 
        greedy, move to elimate the max / min gap at two ends 

        To get max
        greedy, move the min gap, to the other end, so the other end has better chance
        to become min gap

        To get min
        greedy, move the max gap, to the other end, so the other end's other end has 
        better chance become max gap
        """
        stones.sort()
        gaps = [stones[i + 1] - stones[i] - 1 for i in range(len(stones) - 1)]

        # to get max, pop the min gap 
        d = deque(gaps)
        cnt = 0
        while d:
            while d and d[0] == 0:
                d.popleft()
            while d and d[~0] == 0:
                d.pop()

            if not d:
                break 
            if len(d) == 1:
                cnt += d[0]
                d[0] = 0
            elif d[0] > d[~0]:
                d.pop()
                cnt += 1
                d[0] -= 1
                if d[0] > 0:
                    d[0] -= 1
                    d.appendleft(1)
            else:
                cnt += 1
                d.popleft()
                d[~0] -= 1
                if d[~0] > 0:
                    d[~0] -= 1
                    d.append(1)

        # to get min, pop the max gap  
        d = deque(gaps)
        cnt2 = 0
        while d:
            while d and d[0] == 0:
                d.popleft()
            while d and d[~0] == 0:
                d.pop()
            if not d:
                break 
            if len(d) == 1:
                if d[0] >= 2:
                    cnt2 += 2
                else:
                    cnt2 += 1
                d[0] = 0
            elif d[0] > d[~0]:
                d.popleft()
                cnt2 += 1
                d[~0] -= 1
                if d[~0] > 0:
                    d[~0] -= 1
                    d.append(1)
            else:
                cnt2 += 1
                d.pop()
                d[0] -= 1
                if d[0] > 0:
                    d[0] -= 1
                    d.appendleft(1)

        return cnt2, cnt



            
        
