"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
 

Constraints:

1 <= nums.length, k <= 10^5
-104 <= nums[i] <= 10^4
"""
import sys 
from collections import deque


class Solution:
    def maxResultTLE(self, A: List[int], k: int) -> int:
        """
        DP
        Let F[i] be the maximum at A[i]
         F[i] = A[i] + max(
            F[i-1]
            F[i-2]
            ...
            F[i-k]
         )
        """
        N = len(A)
        F = [-sys.maxsize-1 for _ in range(N)]
        F[0] = A[0]
        for i in range(1, N):
            for j in range(i-1, max(0, i-k) -1, -1):
                F[i] = max(F[i], F[j])
            F[i] += A[i]

        return F[~0]
    
    def maxResult(self, A: List[int], k: int) -> int:
        """
        DP
        Let F[i] be the maximum at A[i]
         F[i] = A[i] + max(
            F[i-1]
            F[i-2]
            ...
            F[i-k]
         )
        use monotonic queue to keep track the max in window F[i-k:i]
        """
        N = len(A)
        F = [-sys.maxsize-1 for _ in range(N)]
        F[0] = A[0]
        q = deque()  # max, monotonic decreasing to keep track 1st, 2nd, 3rd largest
        for i in range(1, N):
            # processing F[i-1]
            while q and F[q[~0]] <= F[i-1]:
                q.pop()
            q.append(i-1)

            # indices falling out of window
            while q and q[0] < i - k:
                q.popleft()
           
            F[i] = A[i] + F[q[0]]

        return F[~0]