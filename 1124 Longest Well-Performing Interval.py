"""
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0
 

Constraints:

1 <= hours.length <= 10^4
0 <= hours[i] <= 16
"""
class Solution:
    def longestWPI_TLE(self, hours: List[int]) -> int:
        """
        Use a stack to hold tiring day?

        Not necessarily

        use prefix sum 
        """
        A = [1 if hour > 8 else -1 for hour in hours]
        N = len(A)
        prefix = [0 for _ in range(N+1)]  # A[:i]
        for i in range(1, N+1):
            prefix[i] = prefix[i-1] + A[i-1]
        
        ret = 0
        for i in range(N+1):  # not from 1
            for j in range(i+1, N+1):
                if prefix[j] - prefix[i] > 0:
                    ret = max(ret, j - i)
        
        return ret
    
    def longestWPI(self, hours: List[int]) -> int:
        """
        use prefix sum + monotonic stack 
        """
        A = [1 if hour > 8 else -1 for hour in hours]
        N = len(A)
        prefix = [0 for _ in range(N+1)]  # A[:i]
        for i in range(1, N+1):
            prefix[i] = prefix[i-1] + A[i-1]

        stk = []  # monotonic decreasing stack with increasing index
        for i in range(N+1):
            if not stk or prefix[stk[~0]] > prefix[i]:
                stk.append(i)
        
        ret = 0
        for j in range(N, 0, -1):
            while stk and prefix[j] - prefix[stk[~0]] > 0:
                i = stk.pop()
                ret = max(ret, j - i)
        
        return ret