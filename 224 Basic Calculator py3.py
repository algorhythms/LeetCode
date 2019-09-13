#!/usr/bin/python3
"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus +
or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        """
        1. treat +/- as unary operator
        2. maintain stk of operands to sum
        3. handle bracket recursively
        """
        ret, _ = self.eval(s + "\0", 0, [])
        return ret

    def eval(self, s: str, start: int, stk: List[int]) -> int:
        prev_op = "+"
        operand = 0
        i = start
        while i < len(s):  #  not using for-loop, since the cursor needs to advance in recursion
            if s[i] == " ":
                pass
            elif s[i].isdigit():
                operand = operand * 10 + int(s[i])
            elif s[i] in ("+", "-", ")", "\0"):  # delimited
                if prev_op == "+":
                    stk.append(operand)
                elif prev_op == "-":
                    stk.append(-operand)
        
                if s[i] in ("+", "-"):
                    operand = 0
                    prev_op = s[i]
                elif s[i] in (")", "\0"):
                    return sum(stk), i
            elif s[i] == "(":
                # avoid setting operand to 0
                operand, i = self.eval(s, i + 1, [])
            else:
                raise

            i += 1


if __name__ == "__main__":
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
