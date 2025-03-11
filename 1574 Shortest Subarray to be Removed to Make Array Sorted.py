"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
"""
import bisect


class SolutionAdditionalMemory:
    def findLengthOfShortestSubarray_suboptimal(self, A: List[int]) -> int:
        """
        It is subarray, not subsequence. For subsequence, may use DP

        Has to be sorted
        [1,2,3,10,4,2,3,5]
        option1: [1,2,3,10]
        option2: [1,2,3,4,5]

        next larger element?
         0 1 2 3  4 5 6 7 8
        [1,2,3,10,4,2,3,5]
        [2,3,10,\0,5,3,5,\0]
        [1,2,3,8, 8,6,7,8]
        
        (val, idx)
        does not work , since (3, 2) need to consider (2, 5)

        Complementary:
        find the longest increasing subarray prefix 
        find the longest increasing subarray suffix

        then keep popping either stack to make a single subarray increasing
        prefix: [1, 2, 3, 10]
        suffix: [5, 3, 2]
        O(N^2) to search the stack
        or bisect O(N logN)
        """
        prefix = []
        for a in A:
            if not prefix or prefix[-1] <= a:
                prefix.append(a)
            else:
                break
        suffix = []
        for a in A[::-1]:
            if not suffix or suffix[-1] >= a:
                suffix.append(a)
            else:
                break 
                
        maxa = 0
        p = list(prefix)
        # bisect only works on asc array 
        suffix_rev = suffix[::-1]
        while p:
            t = p[-1]
            idx = bisect.bisect_right(suffix_rev, t)
            maxa = max(maxa, len(p) + len(suffix_rev) - idx)
            p.pop()
        s = list(suffix)
        while s:
            t = s[-1]
            idx = bisect.bisect_right(prefix, t)
            maxa = max(maxa, len(s) + idx)
            s.pop()
        
        return max(0, len(A) - maxa)  # handle double counting of the same element
    
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        """
        prefix: [1, 2, 3, 10]
        suffix: [5, 3, 2]

        Bridge the two sorted arrays can be O(N)
        """
        prefix = []
        for a in A:
            if not prefix or prefix[-1] <= a:
                prefix.append(a)
            else:
                break
        suffix = []
        for a in A[::-1]:
            if not suffix or suffix[-1] >= a:
                suffix.append(a)
            else:
                break 

        maxa = max(len(suffix), len(prefix))
        j = len(suffix) - 1
        for i in range(len(prefix)):
            # this does not handle empty prefix
            while j >= 0 and suffix[j] < prefix[i]:
                j -= 1
            maxa = max(maxa, i+1 + j+1)

        return max(0, len(A) - maxa)  # handle double counting of the same element


class Solution:
    def findLengthOfShortestSubarray(self, A: List[int]) -> int:
        """
        Use pointers instead of additional memory

        Bridget two asc sorted list 
        [1, 2, 3, 4, 5]
        [3, 4, 5]
        """
        N = len(A)

        # sorted: A[:prefix]
        prefix = 0
        for i in range(N):
            if prefix == 0 or A[i] >= A[prefix-1]:
                prefix = i + 1
            else:
                break 

        # sorted: A[suffix:]
        suffix = N
        for i in range(N-1, -1, -1):
            if suffix == N or A[i] <= A[suffix]:
                suffix = i
            else:
                break 

        if prefix > suffix:
            return 0

        maxa = 0
        j = suffix
        for i in range(prefix+1):
            while i-1 >= 0 and j < N and A[i-1] > A[j]:
                j += 1

            maxa = max(maxa, i+(N-j))
        
        return N - maxa