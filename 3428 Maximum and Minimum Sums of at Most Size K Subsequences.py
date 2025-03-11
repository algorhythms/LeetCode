"""
You are given an integer array nums and a positive integer k. Return the sum of the maximum and minimum elements of all 
subsequences of nums with at most k elements.

Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:

Input: nums = [1,2,3], k = 2

Output: 24

Explanation:

The subsequences of nums with at most 2 elements are:

Subsequence	Minimum	Maximum	Sum
[1]	1	1	2
[2]	2	2	4
[3]	3	3	6
[1, 2]	1	2	3
[1, 3]	1	3	4
[2, 3]	2	3	5
Final Total	 	 	24
The output would be 24.

Example 2:

Input: nums = [5,0,6], k = 1

Output: 22

Explanation:

For subsequences with exactly 1 element, the minimum and maximum values are the element itself. Therefore, the total is 5 + 5 + 0 + 0 + 6 + 6 = 22.

Example 3:

Input: nums = [1,1,1], k = 2

Output: 12

Explanation:

The subsequences [1, 1] and [1] each appear 3 times. For all of them, the minimum and maximum are both 1. Thus, the total is 12.

 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
1 <= k <= min(70, nums.length)
"""
MOD = int(1e9 + 7)

class Solution:
    def minMaxSums(self, A: List[int], K: int) -> int:
        """
        sort
        calcualte how many subsequence between i, j with i and j selected.  n \choose r
        Select i, j is O(N^2) 

        Contribution based, when select A[i]:
        * A[i] is the min 
        * A[i] is the max
        """
        A.sort()

        N = len(A)
        nCr = [
            [0 for _ in range(K)]
            for _ in range(N+1)
        ]
        # nCr[0][x] must be 0 where x > 0

        nCr[0][0] = 1
        for n in range(1, N+1):
            nCr[n][0] = 1
            for r in range(1, K):
                nCr[n][r] = nCr[n-1][r-1] + nCr[n-1][r]

        ret = 0
        for i in range(N):
            # choose A[i]
            sequences = 0
            for r in range(K):  # choose up to k-1 items 
                if r <= i:
                    sequences += nCr[i][r]
                else:
                    break 
            
            ret += A[i] * sequences  # A[i] is the max
            ret += A[~i] * sequences # A[~i] is the min
            ret %= MOD

        return ret 