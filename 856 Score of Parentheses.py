#!/usr/bin/python3
"""
Given a balanced parentheses string S, compute the score of the string based on
the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        """
        stk

        Every position in the string has a depth - some number of matching
        parentheses surrounding it
        """
        stk = []
        ret = 0
        for s in S:
            if s == "(":
                stk.append(0)
            else:
                cur = stk.pop()
                score = max(2 * cur, 1)
                if stk:
                    stk[-1] += score
                else:
                    ret += score

        return ret

    def scoreOfParentheses_error(self, S: str) -> int:
        """
        stk
        """
        ret = 0
        cur_stk = []
        for s in S:
            if s == "(":
                cur_stk.append(0)
                stk.append(s)
            else:
                stk.pop()
                if cur_stk[-1] == 0:
                    cur_stk[-1] = 1
                else:
                    cur_stk[-1] *= 2
            if not stk:
                ret += cur
                cur = 0

        return ret


if __name__ == "__main__":
    assert Solution().scoreOfParentheses("(())") == 2
    assert Solution().scoreOfParentheses("(()(()))") == 6
