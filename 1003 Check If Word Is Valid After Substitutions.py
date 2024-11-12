#!/usr/bin/python3
"""
Given a string s, determine if it is valid.

A string s is valid if, starting with an empty string t = "", you can transform t into s after performing the following operation any number of times:

Insert string "abc" into any position in t. More formally, t becomes tleft + "abc" + tright, where t == tleft + tright. Note that tleft and tright may be empty.
Return true if s is a valid string, otherwise, return false.

 

Example 1:

Input: s = "aabcbc"
Output: true
Explanation:
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
Example 2:

Input: s = "abcabcababcc"
Output: true
Explanation:
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
Example 3:

Input: s = "abccba"
Output: false
Explanation: It is impossible to get "abccba" using the operation.
 

Constraints:

1 <= s.length <= 2 * 104
s consists of letters 'a', 'b', and 'c'
"""

from collections import defaultdict

class Solution:
    def isValid_naive(self, s: str) -> bool:
        """
        similar to valid parenthesis of ()
        cnt[a] >= cnt[b] >= cnt[c]
        in the end, cnt[a] == cnt[b] == cnt[c]
        but aaabbbccc is invalid 

        remove "abc", there another "abc" in the string. O(N^2)
        """
        if len(s) == 0:
            return True 
        
        for i in range(len(s) - 2):
            if s[i:i+3] == "abc":
                return self.isValid(s[:i] + s[i+3:])
        
        return False

    def isValid(self, s: str) -> bool:
        """
        when c, we there must be a and b immediately before
        using stk
        """
        stk = []
        for e in s:
            if e in ("a", "b"):
                stk.append(e)
            else:  # "c"
                if len(stk) < 2:
                    return False 
                if stk.pop() != "b":
                    return False
                if stk.pop() != "a":
                    return False
            
        return len(stk) == 0