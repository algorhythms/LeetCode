"""
You are given an array nums of length n. You are also given an integer k.

You perform the following operation on nums once:

Select a 
subarray
 nums[i..j] where 0 <= i <= j <= n - 1.
Select an integer x and add x to all the elements in nums[i..j].
Find the maximum frequency of the value k after the operation.

 

Example 1:

Input: nums = [1,2,3,4,5,6], k = 1

Output: 2

Explanation:

After adding -5 to nums[2..5], 1 has a frequency of 2 in [1, 2, -2, -1, 0, 1].

Example 2:

Input: nums = [10,2,3,4,5,5,4,3,2,2], k = 10

Output: 4

Explanation:

After adding 8 to nums[1..9], 10 has a frequency of 4 in [10, 10, 11, 12, 13, 13, 12, 11, 10, 10].

 

Constraints:

1 <= n == nums.length <= 10^5
1 <= nums[i] <= 50
1 <= k <= 50
"""
class Solution:
    def maxFrequency_TLE(self, nums: List[int], k: int) -> int:
        """
        Brute foce:
        * i, j subarray search, the max frequency of equal distance to k 
        * O(N^3)

        k is in [1, 50]
        Does k actually matter? It matters for the rest of the array without operations
        Define O[i]: In nums[:i], the frequency of number = k
        Define F[i][j]: In nums[:i], the frequency of number = j+1
        O(N^2)
        """
        n = len(nums)
        O = [0 for _ in range(n+1)]
        for i in range(n):
            O[i+1] = O[i]
            if nums[i] == k:
                O[i+1] += 1
        
        F = [
            [0 for _ in range(50)]
            for _ in range(n+1)
        ]
        for i in range(n):
            F[i+1] = list(F[i])  # copy 
            F[i+1][nums[i] - 1] += 1

        maxa = 0
        for i in range(n):
            for j in range(i+1, n+1):
                # subarray nums[i:j]
                cnt = 0
                cnt += O[i]
                cnt += O[n] - O[j]

                m = 0
                for num in range(50):
                    m = max(m, F[j][num] - F[i][num])

                maxa = max(maxa, cnt + m)
        
        return maxa
    
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        Maximum subarray frequency -> Maximum subarray sum
        """
        n = len(nums)
        freq_k = 0
        for n in nums:
            if n == k:
                freq_k += 1
        
        maxa = 0
        for target in range(1, 51):
            maxa = max(maxa, self.count(nums, target, k) + freq_k)
        
        return maxa
    
    def count(self, nums, target, k):
        cnt = 0
        maxa = 0
        for n in nums:
            if n == k:
                cnt -= 1
            elif n == target:
                cnt += 1

            if cnt < 0:
                cnt = 0

            maxa = max(maxa, cnt)

        return maxa