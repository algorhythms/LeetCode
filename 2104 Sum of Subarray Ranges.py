"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 10^9
 

Follow-up: Could you find a solution with O(n) time complexity?
"""
import sys


class Solution:
    def subArrayRanges_brute(self, A: List[int]) -> int:
        """
        Get a range -> get the min and max
        Get all subarrays -> iterate i and j, keep tracks of min and max -> O(N^2)

        Get a range over a sliding window -> monotonic queue?

        Brute force 
        """
        N = len(A)
        ret = 0
        for i in range(N):
            mini = A[i]
            maxa = A[i]
            for j in range(i+1, N):
                mini = min(mini, A[j])
                maxa = max(maxa, A[j])
                ret += maxa - mini
        
        return ret
    
    def subArrayRanges(self, A: List[int]) -> int:
        """
        Get a range -> get the min and max
        Get all subarrays -> iterate i and j, keep tracks of min and max -> O(N^2)
        \sum{range} 
        = \sum{max - min}
        = \sum max - \sum min
        \sum min
        = #times of min * min val
        = #times of local min * min val
        <- find the boundary of local min
        <- monotonic stk 
        """
        N = len(A)
        ret = 0

        sum_max = 0
        stk = []  # monotonically decreasing stk for local max
        A.append(sys.maxsize)
        for i in range(N+1):
            while stk and A[stk[-1]] < A[i]:
                mid = stk.pop()
                lo = stk[-1] if stk else -1
                # times: [mid, i), (lo, mid]
                cnt = (i - mid) * (mid - lo)
                sum_max += cnt * A[mid]
            stk.append(i)
        A.pop()

        sum_min = 0
        stk = []  # monotonically increasing stk for local min
        A.append(-sys.maxsize-1)
        for i in range(N+1):
            while stk and A[stk[-1]] > A[i]:
                mid = stk.pop()
                lo = stk[-1] if stk else -1
                # times: [mid, i), (lo, mid]
                cnt = (i-mid) * (mid - lo)
                sum_min += cnt * A[mid]
            stk.append(i)
        A.pop()
        
        return sum_max - sum_min
