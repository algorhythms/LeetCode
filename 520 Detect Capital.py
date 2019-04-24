#!/usr/bin/python3
"""
Given a word, you need to judge whether the usage of capitals in it is right or
not.

We define the usage of capitals in a word to be right when one of the following
cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter,
like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase
latin letters.
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Two passes is easy
        How to do it in one pass
        """
        if not word:
            return True

        head_upper = word[0].isupper()

        # except for the head
        has_lower = False
        has_upper = False
        for w in word[1:]:
            if w.isupper():
                has_upper = True
                if has_lower or not head_upper:
                    return False
            else:
                has_lower = True
                if has_upper:
                    return False
        return True
