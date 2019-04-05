#!/usr/bin/python3
"""
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
odd.
That is, the subarray is turbulent if the comparison sign flips between each
adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
"""
from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        """
        scan
        """
        flag = None  # 0: expecting <, 1: expecting > 
        ret = 1
        cur = 1
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                flag = None
                cur = 1
            elif A[i] > A[i+1]:
                if flag is None or flag == 1:
                    cur += 1
                    ret = max(ret, cur)
                else:
                    cur = 2
                flag = 0
            else:  # <
                if flag is None or flag == 0:
                    cur += 1
                    ret = max(ret, cur)
                else:
                    cur = 2
                flag = 1

        return ret


if __name__ == "__main__":
    assert Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9]) == 5
