"""
You are given an array of integers nums of size 3.

Return the maximum possible number whose binary representation can be formed by concatenating the binary representation of all elements in nums in some order.

Note that the binary representation of any number does not contain leading zeros.

 

Example 1:

Input: nums = [1,2,3]

Output: 30

Explanation:

Concatenate the numbers in the order [3, 1, 2] to get the result "11110", which is the binary representation of 30.

Example 2:

Input: nums = [2,8,16]

Output: 1296

Explanation:

Concatenate the numbers in the order [2, 8, 16] to get the result "10100010000", which is the binary representation of 1296.

 

Constraints:

nums.length == 3
1 <= nums[i] <= 127
"""
class Solution:
    def maxGoodNumber_error(self, nums: List[int]) -> int:
        """
        11
        101
        10001
        1010101

        just sort by lexical order

        but 1 should be in front of 10
        """
        nums_bin_str = [str(bin(n))[2:] for n in nums]
        nums_bin_str.sort(reverse=True)
        return int("".join(nums_bin_str), 2)
    
    def maxGoodNumber(self, nums: List[int]) -> int:
        """
        generate all permutation
        """
        # '0b101'
        nums_bin_str = [str(bin(n))[2:] for n in nums]
        ret = []
        self.permutations(nums_bin_str, 0, ret)
        return max(
            [int("".join(n), 2) for n in ret]
        )
    
    def permutations(self, A, cur, ret):
        # in-place itertools.permutations 
        if cur == len(A):
            ret.append(list(A))  # clone
            return
        
        for i in range(cur, len(A)):
            # swap
            A[cur], A[i] = A[i], A[cur]
            self.permutations(A, cur+1, ret)
            # restore
            A[i], A[cur] = A[cur], A[i]
