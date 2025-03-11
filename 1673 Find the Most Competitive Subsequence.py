"""
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
Example 2:

Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
1 <= k <= nums.length
"""
class Solution:
    def mostCompetitive(self, A: List[int], k: int) -> List[int]:
        """
        sort and get the min?
        subsequence still maintain the order

        find the next smaller number of each element
        build the k-size subsequence from next smaller element 
        then take the min
        O(NK)

        Can we reduce time compexlity?
        short curcit when reach A[N_K:K]
        sort, start from smallest O(N logN)

        Can we do better?
        Monotonic stack in one pass 
        Different than finding the next smaller number
        """
        # monotonically increasing stk as the result
        stk = []
        N = len(A)
        for i in range(N):
            # remaining >= required 
            while stk and A[stk[-1]] > A[i] and N - i >= k - (len(stk) - 1):
                stk.pop()
            stk.append(i)
        
        ret = [A[stk[i]] for i in range(k)]
        return ret