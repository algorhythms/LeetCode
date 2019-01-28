#!/usr/bin/python3
"""
Given a circular array (the next element of the last element is the first
element of the array), print the Next Greater Number for every element. The Next
Greater Number of a number x is the first greater number to its traversing-order
next in the array, which means you could search circularly to find its next
greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""
from bisect import bisect


class Solution:
    def nextGreaterElements(self, nums):
        """
        scan the nums from right to left, since next largest number, you can
        drop certain information about the A[i:]. Use stack to keep a increasing
        numbers. if A[i] > any A[i+1: j] but A[i] < A[j], we can safely drop
        the numbers A[i+1:j] since they won't be useful.

        :type nums: List[int]
        :rtype: List[int]
        """
        # initalize the stack
        stk = []
        for n in nums[::-1]:
            while stk and stk[-1] <= n:
                stk.pop()
            stk.append(n)

        ret = []
        for n in nums[::-1]:
            while stk and stk[-1] <= n:
                stk.pop()
            ret.append(stk[-1] if stk else -1)
            stk.append(n)

        return ret[::-1]

    def nextGreaterElements_error(self, nums):
        """
        brute force O(n^2)

        bisect O(n lgn) - error cannot binary search
        :type nums: List[int]
        :rtype: List[int]
        """
        A = nums + nums
        print(A)
        ret = []
        for e in nums:
            t = bisect(A, e)
            if t == len(A):
                ret.append(-1)
            else:
                ret.append(A[t])

        print(ret)
        return ret


if __name__ == "__main__":
    assert Solution().nextGreaterElements([1,2,1]) == [2, -1, 2]
