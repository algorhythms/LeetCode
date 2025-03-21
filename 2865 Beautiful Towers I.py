"""
You are given an array heights of n integers representing the number of bricks in n consecutive towers. Your task is to remove some bricks to form a mountain-shaped tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.

Return the maximum possible sum of heights of a mountain-shaped tower arrangement.

 

Example 1:

Input: heights = [5,3,4,1,1]

Output: 13

Explanation:

We remove some bricks to make heights = [5,3,3,1,1], the peak is at index 0.

Example 2:

Input: heights = [6,5,3,9,2,7]

Output: 22

Explanation:

We remove some bricks to make heights = [3,3,3,9,2,2], the peak is at index 3.

Example 3:

Input: heights = [3,2,5,5,2,3]

Output: 18

Explanation:

We remove some bricks to make heights = [2,2,5,5,2,2], the peak is at index 2 or 3.

 

Constraints:

1 <= n == heights.length <= 10^3
1 <= heights[i] <= 10^9
"""
class Solution:
    def maximumSumOfHeights_brute(self, H: List[int]) -> int:
        """
        Select a peak
        then make mountain-shaped using stack

        Get the heighest 
        O(N^2)
        """
        maxa = 0
        N = len(H)
        for p in range(N):  # peak 
            L_stk = [p]
            for i in range(p-1, -1, -1):
                if H[i] > H[L_stk[-1]]:
                    L_stk.append(L_stk[-1])
                else:
                    L_stk.append(i)
            R_stk = [p]
            for i in range(p+1, N):
                if H[i] > H[R_stk[-1]]:
                    R_stk.append(R_stk[-1])
                else:
                    R_stk.append(i)
            cur = sum(H[i] for i in L_stk  +R_stk) - H[p]
            maxa = max(maxa, cur)

        return maxa
    
    def maximumSumOfHeights(self, H: List[int]) -> int:
        """
        O(N)
        Consider 1 side of the problem, from left to peak 
        Let L[i] be the max sum of upward-shaped area ended at index i
        Maintain a monotonically increasing stack
        A[lo] < A[mid] > A[i]
        A[mid] is the local min for (lo, mid]
        when popping mid:
            area -= (mid - lo) * A[mid]
            # note: not area -= (i - (lo+1)) * A[mid] 
            # for mid as local min as (lo, i)
            # since mid has not impact on (mid, i)
        A[i] is the new local min for (lo, i]
            area += (i - lo) * A[i]

        same for R when scanning from right to peak
        """
        L = self.dp(H)
        R = self.dp(H[::-1])
        maxa = 0
        for i in range(len(H)):
            cur = L[i] + R[~i] - H[i]  # double count H[i]
            maxa = max(maxa, cur)

        return maxa
    
    def dp(self, H):
        N = len(H)
        L = [0 for _ in range(N)]
        stk = []  # mono asc
        H.append(-sys.maxsize-1)
        cur = 0
        for i in range(N):
            while stk and H[stk[-1]] > H[i]:
                mid = stk.pop()
                lo = stk[-1] if stk else -1
                cur -= (mid - lo) * H[mid]

            lo = stk[-1] if stk else -1
            cur += (i-lo) * H[i]  # (lo, i]
            L[i] = cur
            stk.append(i)

        H.pop()
        return L