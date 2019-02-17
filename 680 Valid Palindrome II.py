#!/usr/bin/python3
"""
Given a non-empty string s, you may delete at most one character. Judge whether
you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the
string is 50000.
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Brute force, delete and check. O(n^2)

        Start from start and end, then check equal. If not match, skip either
        side (i.e. delete a character), then check palindrome
        """
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                # error, for -1, start > end. Indexing is like range
                # return s[i:j] == s[i:j:-1] or s[i+1:j+1] == s[i+1:j+1:-1]
                return self.is_palindrome(s[i:j]) or self.is_palindrome(s[i+1:j+1])

        return True

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    assert Solution().validPalindrome("aba") == True
    assert Solution().validPalindrome("abca") == True
