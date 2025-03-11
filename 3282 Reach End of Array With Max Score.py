"""
You are given an integer array nums of length n.

Your goal is to start at index 0 and reach index n - 1. You can only jump to indices greater than your current index.

The score for a jump from index i to index j is calculated as (j - i) * nums[i].

Return the maximum possible total score by the time you reach the last index.

 

Example 1:

Input: nums = [1,3,1,5]

Output: 7

Explanation:

First, jump to index 1 and then jump to the last index. The final score is 1 * 1 + 2 * 3 = 7.

Example 2:

Input: nums = [4,3,1,3,2]

Output: 16

Explanation:

Jump directly to the last index. The final score is 4 * 4 = 16.

 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
class Solution:
    def findMaximumScore(self, A: List[int]) -> int:
        """
        F[i] max score at A[i]

        F[i] = max(F[j] + (i - j)*A[j] for all j)
        O(N^2)

        Score: (i-j) * A[i]
        sum(i-j for all i, j) = len(A) - 1
        Sum of jump gap sizes is constant
        
        It can be proven that from each index i, the optimal solution is to jump to the nearest index j > i 
        such that nums[j] > nums[i].

        Greedy: 
        * Solo jump vs. double jump
        * maximize gap value, gap value defined by the original A[i] -> find the next larger A[j]
        * as long as the next A[j] > A[i], then there is a net gain
        """
        i = 0
        ret = 0
        for j in range(1, len(A)):
            if A[j] > A[i] or j == len(A)-1:
                ret += (j - i) * A[i]
                i = j
            # handle end of iteration

        return ret

