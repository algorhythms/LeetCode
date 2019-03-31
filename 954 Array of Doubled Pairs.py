#!/usr/bin/python3
"""
Given an array of integers A with even length, return true if and only if it is
possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every
0 <= i < len(A) / 2.



Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
[2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false


Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""
from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort(key=abs)
        counter = Counter(A)
        for a in A:
            if counter[a] == 0:
                continue
            if counter[2*a] == 0:
                return False

            counter[a] -= 1
            counter[2*a] -= 1

        return True

    def canReorderDoubled_positive_negative(self, A: List[int]) -> bool:
        """
        sort + counter to form the doubled pairs
        """
        A.sort()
        counter = Counter(A)
        for a in A:
            if counter[a] == 0:
                continue
            counter[a] -= 1
            if a > 0:
                target = 2 * a
            elif a % 2 != 0:
                return False
            else:
                target = a // 2

            if counter[target] > 0:
                counter[target] -= 1
            else:
                return False

        return True


if __name__ == "__main__":
    assert Solution().canReorderDoubled([4,-2,2,-4]) == True
