"""
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
from collections import deque


class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        """
        Keep track the max in a sliding window -> use a monotonic queue
        * when iterating j, q represent the max indicies in the window ending at j

        monotonic queue
        """
        q_max = deque() # q_max[0] represent the current max, monotonically decreasing 
        q_min = deque() # q_min[0] represent the current min, monotonically increasing
        i = 0  # left 
        j = 0  # right 
        ret = 0

        while j < len(A):
            # process A[j]
            while q_max and A[q_max[~0]] <= A[j]:
                q_max.pop()
            q_max.append(j)
            while q_min and A[q_min[~0]] >= A[j]:
                q_min.pop()
            q_min.append(j)

            while q_max and q_min and A[q_max[0]] - A[q_min[0]] > limit:
                # q need to store indices
                # move to the smaller index 
                if q_max[0] < q_min[0]:
                    i = q_max.popleft() + 1
                else:
                    i = q_min.popleft() + 1
                
            l = j - i + 1
            ret = max(ret, l)
            j += 1

        return ret