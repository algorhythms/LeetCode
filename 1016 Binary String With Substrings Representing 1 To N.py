#!/usr/bin/python3
"""
Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "0110", n = 3
Output: true
Example 2:

Input: s = "0110", n = 4
Output: false
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= n <= 10^9
"""

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        """
        Naive solution: KMP string matching from 1 to N, O(N * (m + n)).
        Python `in` is enough

        Construct numbers from the string s itself
        Scan the s from left to right 
        """
        numbers = set()
        for i in range(len(s)):
            cur = 0
            sig = 1
            for j in range(i, len(s)):
                if s[~j] == "1":
                    cur += sig
                if cur > n:
                    break

                sig <<= 1
                
                if cur != 0:
                    numbers.add(cur)
        
        return len(numbers) == n
