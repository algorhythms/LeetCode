#!/usr/bin/python3
"""
Given a non-negative integer, you could swap two digits at most once to get the
maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        stk maintain a increasing stack from right to left
        """
        stk = []
        nums = list(str(num))
        n = len(nums)
        for i in range(n-1, -1, -1):
            if stk and stk[-1][1] >= nums[i]:  # only keep the rightmost duplicate
                continue
            stk.append((i, nums[i]))

        for i in range(n):
            while stk and stk[-1][0] <= i:
                stk.pop()
            if stk and stk[-1][1] > nums[i]:
                j = stk[-1][0]
                nums[i], nums[j] = nums[j], nums[i]
                break

        return int("".join(nums))


if __name__ == "__main__":
    assert Solution().maximumSwap(2736) == 7236
    assert Solution().maximumSwap(9973) == 9973
