#!/usr/bin/python3
"""
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity
of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left
parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Brute force: dfs branching on "*".

        Better Solution:
        keep two stack: stak of "(" and stack of "*"
        """
        stk_left = []
        stk_star = []
        for i, c in enumerate(s):
            if c == "(":
                stk_left.append(i)
            elif c == "*":
                stk_star.append(i)
            else:
                if stk_left:
                    stk_left.pop()
                elif stk_star:
                    stk_star.pop()
                else:
                    return False

        while stk_left and stk_star and stk_star[-1] > stk_left[-1]:
            stk_star.pop()
            stk_left.pop()

        return not stk_left


if __name__ == "__main__":
    assert Solution().checkValidString("(*))") == True
    assert Solution().checkValidString("*(") == False
    assert Solution().checkValidString("(*)") == True
