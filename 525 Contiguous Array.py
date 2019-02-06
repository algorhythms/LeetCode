#!/usr/bin/python3
"""
Given a binary array, find the maximum length of a contiguous subarray with
equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""


class Solution:
    def findMaxLength(self, nums):
        """
        Look back with map

        key: map stores the difference of the 0, 1 count
        Similar to contiguous sum to target
        :type nums: List[int]
        :rtype: int
        """
        o = 0
        z = 0
        d = {0: 0}  # diff for nums[:l]
        ret = 0
        for i, e in enumerate(nums):
            if e == 1:
                o += 1
            else:
                z += 1
            diff = o - z
            if diff in d:
                ret = max(ret, i + 1 - d[diff])
            else:
                d[diff] = i + 1

        return ret

    def findMaxLength_error(self, nums):
        """
        starting from both sides, shrinking until equal

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        F = [0 for _ in range(n+1)]
        for i in range(n):
            F[i+1] = F[i]
            if nums[i] == 0:
                F[i+1] += 1

        i = 0
        j = n
        while i < j:
            count = F[j] - F[i]
            l = j - i
            if count * 2 == l:
                print(l)
                return l
            elif count * 2 < l:
                if nums[i] == 1:
                    i += 1
                else:
                    j -= 1
            else:
                if nums[i] == 0:
                    i += 1
                else:
                    j -= 1
        return 0


    def findMaxLength_TLE(self, nums):
        """
        scan nums[i:j], check number of 0 (pre-calculated)
        O(n^2)

        :type nums: List[int]
        :rtype: int
        """
        F = [0]
        n = len(nums)
        for e in nums:
            if e == 0:
                F.append(F[-1] + 1)
            else:
                F.append(F[-1])

        ret = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if (F[j] - F[i]) * 2 == j - i:
                    ret = max(ret, j - i)

        return ret


if __name__ == "__main__":
    assert Solution().findMaxLength([0, 1, 0]) == 2
    assert Solution().findMaxLength([0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]) == 68
