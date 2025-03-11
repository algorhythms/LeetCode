"""
You are given a 0-indexed integer array nums. A subarray of nums is called continuous if:

Let i, i + 1, ..., j be the indices in the subarray. Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
Return the total number of continuous subarrays.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [5,4,2,4]
Output: 8
Explanation: 
Continuous subarray of size 1: [5], [4], [2], [4].
Continuous subarray of size 2: [5,4], [4,2], [2,4].
Continuous subarray of size 3: [4,2,4].
There are no subarrys of size 4.
Total continuous subarrays = 4 + 3 + 1 = 8.
It can be shown that there are no more continuous subarrays.
 

Example 2:

Input: nums = [1,2,3]
Output: 6
Explanation: 
Continuous subarray of size 1: [1], [2], [3].
Continuous subarray of size 2: [1,2], [2,3].
Continuous subarray of size 3: [1,2,3].
Total continuous subarrays = 3 + 2 + 1 = 6.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
import heapq


class SolutionHeap:
    def continuousSubarrays(self, A: List[int]) -> int:
        """
        Need to maintain max and min in the sliding window
        -> heap 
        
        
        In sliding window, count of all valid subarrays ending AT j
        -> j - i + 1
        """
        ret = 0
        i = 0  # starting index of the window
        j = 0  # ending index of the window
        h_min = []  # (a, idx)
        h_max = []  # (-a, idx)
        while j < len(A):
            heapq.heappush(h_min, (A[j], j))
            heapq.heappush(h_max, (-A[j], j))
            while -h_max[0][0] - h_min[0][0] > 2:
                # shrink
                i += 1
                while h_min[0][1] < i:
                    heapq.heappop(h_min)
                while h_max[0][1] < i:
                    heapq.heappop(h_max)
            
            ret += j-i+1
            j += 1
        
        return ret
    

from collections import deque


class Solution:
    def continuousSubarrays(self, A: List[int]) -> int:
        """
        Track min & max -> Monotonic Queue
        """
        q_max = deque()  # monotonically decreasing
        q_min = deque()  # monotonically increasing
        i = 0
        j = 0
        ret = 0
        while j < len(A):
            # process A[j]
            while q_max and A[q_max[~0]] <= A[j]:
                q_max.pop()
            q_max.append(j)
            while q_min and A[q_min[~0]] >= A[j]:
                q_min.pop()
            q_min.append(j)
            while q_max and q_min and A[q_max[0]] - A[q_min[0]] > 2:
                # shrink to pass the breaking idx
                if q_max[0] < q_min[0]:
                    prev = q_max.popleft()
                    i = prev + 1
                else:
                    prev = q_min.popleft()
                    i = prev + 1
            
            ret += j - i + 1
            j += 1
            
        return ret 

