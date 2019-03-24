#!/usr/bin/python3
"""
We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we
take the bitwise OR of all the elements in B, obtaining a result A[i] | A[i+1]
| ... | A[j].

Return the number of possible results.  (Results that occur more than once are
only counted once in the final answer.)



Example 1:

Input: [0]
Output: 1
Explanation:
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation:
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: [1,2,4]
Output: 6
Explanation:
The possible results are 1, 2, 3, 4, 6, and 7.


Note:

1 <= A.length <= 50000
0 <= A[i] <= 10^9
"""

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        """
        Use a dp array to record OR
        F[i][j]
        O(N^2) TLE

        F[i][j] records the list of the results
        #F[i][j] >= #F[i+1][j] >= #F[i+2][j] since it is monotonously increasing
        The increasing part is by having one more 1 in the bit of any 32 bit of int
        then F[i][j] is at most O(32)
        """
        ret = set()
        cur = set()  # F[0][i]
        for a in A:
            cur = {a | e for e in cur} | {a}
            ret |= cur

        return len(ret)
