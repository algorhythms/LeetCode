#!/usr/bin/python3
"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where
A and B are valid parentheses strings, and + represents string concatenation.
For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not
exist a way to split it into S = A+B, with A and B nonempty valid parentheses
strings.

Given a valid parentheses string S, consider its primitive decomposition:
S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in
the primitive decomposition of S.

Example 1:
Input: "(()())(())"
Output: "()()()"
Explanation:
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

Example 2:
Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation:
The input string is "(()())(())(()(()))", with primitive decomposition
"(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" +
"()(())" = "()()()()(())".

Example 3:
Input: "()()"
Output: ""
Explanation:
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".


Note:
S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""
from collections import deque


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        """
        Primitive parentheses will have equal number of opened and closed
        parentheses.

        Use count
        Exclude the first and last parathesis
        """
        ret = []
        cnt = 0
        for e in S:
            if e == "(":
                cnt += 1
                if cnt > 1:
                    ret.append(e)
            else:
                cnt -= 1
                if cnt > 0:
                    ret.append(e)

        return "".join(ret)


    def removeOuterParentheses_error(self, S: str) -> str:
        """
        stack + deque
        """
        ret = []
        stk = []
        cur_q = deque()
        for e in S:
            if e == "(":
                stk.append(e)
            else:
                prev = stk.pop()
                if stk:
                    cur_q.appendleft(prev)
                    cur_q.append(e)
                else:
                    ret.extend(cur_q)
                    cur_q = deque()

        return "".join(ret)


if __name__ == "__main__":
    assert Solution().removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
