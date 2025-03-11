"""
You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

 

Example 1:

Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.
Example 2:

Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
class Solution:
    def totalSteps_error(self, A: List[int]) -> int:
        """
        use a stack 
        remove A[i] when A[i-1] > A[i]
        it becomes A[lo] < A[i]
        Keep a monotonically increasing stack 
        """
        maxa = 0 
        stk = []  # asc stack
        cur = 0
        for a in A:
            if stk and stk[-1] > a:
                cur += 1
                continue

            stk.append(a)
            maxa = max(maxa, cur)
            cur = 0

        maxa = max(maxa, cur)
        return maxa
    
    def totalSteps_error(self, A: List[int]) -> int:
        """
        How to count the steps?
        Find the next larger on the left 
        """
        N = len(A)
        # next larger on the left 
        L = [i for i in range(N)]
        # pending element has yet to find the larger
        # scanning from right to left
        stk = []  # monotoicallycall decreasing
        for i in range(N-1, -1, -1):
            while stk and A[stk[-1]] < A[i]:
                mid = stk.pop()
                L[mid] = i
            stk.append(i)
        
        maxa = 0 
        for i, v in enumerate(L):
            maxa = max(maxa, i - v)
        
        return maxa

    def totalSteps(self, A: List[int]) -> int:
        """
        How to count the steps?
        Find the next larger on the left? 

        Requrie DP
        Let F[i] be the number of steps A[i] can remove item

        When A[i] is removing A[j] when j > i and A[i] > A[j]
        F[i] += 1
        remaining = F[pi] - F[i]
        if remaining > 0:
            F[i] += remaining
        essentially, F[i] = max(F[i], F[j])

        Example: [14, 13, 2, 6, 13]
        """
        N = len(A)
        F = [0 for _ in range(N)]
        # To find the next larger item
        # Store the pending element has yet not find next larger
        # monotonically decreasing 
        stk = []
        for i in range(N-1, -1, -1):
            while stk and A[stk[-1]] < A[i]:
                pi = stk.pop()
                F[i] += 1
                remaining = F[pi] - F[i]
                if remaining > 0:
                    F[i] += remaining
                # F[i] = max(F[i], F[pi])
            stk.append(i)
        
        return max(F)        
